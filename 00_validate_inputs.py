"""Validate required inputs for the static smart-city comparison project."""

from __future__ import annotations

import argparse
from pathlib import Path

from common import mirror_to_public, status_note, write_json


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", default=".")
    parser.add_argument("--output-root", default="data/processed")
    parser.add_argument("--public-root", default="public/data/processed")
    args = parser.parse_args()

    project_root = Path(args.project_root).resolve()
    output_root = (project_root / args.output_root).resolve()
    public_root = project_root / args.public_root

    checks = {
        "pangyo_boundary": project_root / "data" / "pangyo_boundary.geojson",
        "cheongna_boundary": project_root / "data" / "cheongna_boundary.geojson",
        "metrics_json": project_root / "data" / "metrics.json",
        "nodes_tsv": project_root / "data" / "raw" / "nodes.tsv",
        "links_tsv": project_root / "data" / "raw" / "links.tsv",
    }

    report = {
        "projectRoot": str(project_root),
        "results": {name: path.exists() for name, path in checks.items()},
        "warnings": [],
    }
    for name, exists in report["results"].items():
        if not exists:
            report["warnings"].append(status_note(f"{name} missing"))

    output_path = output_root / "validation_report.json"
    write_json(output_path, report)
    mirror_to_public(output_path, public_root, output_root)


if __name__ == "__main__":
    main()
