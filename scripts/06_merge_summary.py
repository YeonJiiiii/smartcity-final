"""Merge component summaries into one summary_metrics.json file."""

from __future__ import annotations

import argparse
from pathlib import Path

from common import mirror_to_public, read_json, write_json


def safe_read(path: Path) -> dict:
    return read_json(path) if path.exists() else {"status": "missing"}


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
        "project": {
            "title": "데이터로 진단하는 업무지구의 성공과 실패",
            "defaultBaseYear": 2023,
            "timeUnit": "단면 분석"
        },
        "landuse": safe_read(output_root / "landuse_summary.json"),
        "building": safe_read(output_root / "building_summary.json"),
        "socio": safe_read(output_root / "socio_summary.json"),
        "transport": safe_read(output_root / "transport_summary.json")
    }
    output_path = output_root / "summary_metrics.json"
    write_json(output_path, payload)
    mirror_to_public(output_path, public_root, output_root)


if __name__ == "__main__":
    main()
