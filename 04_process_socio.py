"""Transform verified core metrics into a socio-economic summary."""

from __future__ import annotations

import argparse
from pathlib import Path

from common import mirror_to_public, read_json, write_json


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", default=".")
    parser.add_argument("--output-root", default="data/processed")
    parser.add_argument("--public-root", default="public/data/processed")
    args = parser.parse_args()

    project_root = Path(args.project_root).resolve()
    output_root = (project_root / args.output_root).resolve()
    public_root = project_root / args.public_root
    metrics = read_json(project_root / "data" / "metrics.json")

    payload = {
        "status": "verified_user_input",
        "baseYear": metrics.get("baseYear", 2023),
        "regions": {key: value.get("metrics", {}) for key, value in metrics.get("regions", {}).items()}
    }
    output_path = output_root / "socio_summary.json"
    write_json(output_path, payload)
    mirror_to_public(output_path, public_root, output_root)


if __name__ == "__main__":
    main()
