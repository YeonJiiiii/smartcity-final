"""Create land-use summary placeholders until VWorld data is connected."""

from __future__ import annotations

import argparse
from pathlib import Path

from common import mirror_to_public, write_json


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", default=".")
    parser.add_argument("--output-root", default="data/processed")
    parser.add_argument("--public-root", default="public/data/processed")
    args = parser.parse_args()

    project_root = Path(args.project_root).resolve()
    output_root = (project_root / args.output_root).resolve()
    public_root = project_root / args.public_root

    payload = {
        "status": "data_unavailable",
        "reason": "VWorld land-use data not connected",
        "regions": {
            "pangyo": {"zoningComposition": None, "lumEntropy": None, "developmentRealization": None},
            "cheongna": {"zoningComposition": None, "lumEntropy": None, "developmentRealization": None}
        }
    }
    output_path = output_root / "landuse_summary.json"
    write_json(output_path, payload)
    mirror_to_public(output_path, public_root, output_root)


if __name__ == "__main__":
    main()
