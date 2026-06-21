"""Compute subway-network reachability when nodes.tsv and links.tsv are available."""

from __future__ import annotations

import argparse
import csv
import heapq
from pathlib import Path

from common import mirror_to_public, write_json


def dijkstra(graph: dict[str, list[tuple[str, float]]], start: str) -> dict[str, float]:
    queue = [(0.0, start)]
    distances = {start: 0.0}
    while queue:
        cost, node = heapq.heappop(queue)
        if cost > distances.get(node, float("inf")):
            continue
        for nxt, weight in graph.get(node, []):
            new_cost = cost + weight
            if new_cost < distances.get(nxt, float("inf")):
                distances[nxt] = new_cost
                heapq.heappush(queue, (new_cost, nxt))
    return distances


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", default=".")
    parser.add_argument("--output-root", default="data/processed")
    parser.add_argument("--public-root", default="public/data/processed")
    parser.add_argument("--nodes", default="data/raw/nodes.tsv")
    parser.add_argument("--links", default="data/raw/links.tsv")
    parser.add_argument("--pangyo-station", default="판교역")
    parser.add_argument("--compare-station", default="청라국제도시역")
    args = parser.parse_args()

    project_root = Path(args.project_root).resolve()
    output_root = (project_root / args.output_root).resolve()
    public_root = project_root / args.public_root
    nodes_path = project_root / args.nodes
    links_path = project_root / args.links

    if not nodes_path.exists() or not links_path.exists():
        summary = {
            "status": "data_unavailable",
            "reason": "nodes.tsv or links.tsv missing",
            "candidateStations": {
                "pangyo": args.pangyo_station,
                "cheongna": args.compare_station
            }
        }
        geojson = {"type": "FeatureCollection", "features": [], "metadata": summary}
    else:
        graph: dict[str, list[tuple[str, float]]] = {}
        with links_path.open(encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle, delimiter="\t")
            for row in reader:
                start = row.get("fromNode") or row.get("from")
                end = row.get("toNode") or row.get("to")
                weight_text = row.get("time_sec") or row.get("travel_time_sec") or row.get("weight")
                if not start or not end or not weight_text:
                    continue
                graph.setdefault(start, []).append((end, float(weight_text)))
        summary = {
            "status": "partial_success",
            "reason": "graph built, but station-node matching must be customized to actual nodes schema",
            "graphNodeCount": len(graph)
        }
        geojson = {"type": "FeatureCollection", "features": [], "metadata": summary}
        if graph:
            dijkstra(graph, next(iter(graph)))

    summary_path = output_root / "transport_summary.json"
    geojson_path = output_root / "isochrone_30_60.geojson"
    write_json(summary_path, summary)
    write_json(geojson_path, geojson)
    mirror_to_public(summary_path, public_root, output_root)
    mirror_to_public(geojson_path, public_root, output_root)


if __name__ == "__main__":
    main()
