"""Prepare boundary metadata and mirror boundary files for the static app."""

from __future__ import annotations

import argparse
from pathlib import Path

from common import mirror_to_public, read_json, write_json


def feature_count(path: Path) -> int:
    payload = read_json(path)
    return len(payload.get("features", []))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", default=".")
    parser.add_argument("--output-root", default="data/processed")
    parser.add_argument("--public-root", default="public/data/processed")
    args = parser.parse_args()

    project_root = Path(args.project_root).resolve()
    output_root = (project_root / args.output_root).resolve()
    public_root = project_root / args.public_root

    pangyo = project_root / "data" / "pangyo_boundary.geojson"
    cheongna = project_root / "data" / "cheongna_boundary.geojson"

    manifest = {
        "baseYear": 2023,
        "boundaries": {
            "pangyo": {"path": str(pangyo), "featureCount": feature_count(pangyo)},
            "cheongna": {"path": str(cheongna), "featureCount": feature_count(cheongna)},
        },
    }
    output_path = output_root / "boundary_manifest.json"
    write_json(output_path, manifest)
    mirror_to_public(output_path, public_root, output_root)


if __name__ == "__main__":
    main()
