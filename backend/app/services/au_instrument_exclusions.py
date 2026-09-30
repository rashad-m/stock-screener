from __future__ import annotations

import csv
from pathlib import Path


_AU_EXCLUDED_INSTRUMENTS_PATH = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "au_excluded_instruments.csv"
)


def load_au_excluded_instruments() -> dict[str, str]:
    """Load explicitly excluded AU non-common securities."""
    if not _AU_EXCLUDED_INSTRUMENTS_PATH.exists():
        return {}

    excluded: dict[str, str] = {}

    with _AU_EXCLUDED_INSTRUMENTS_PATH.open(
        "r",
        encoding="utf-8",
        newline="",
    ) as handle:
        reader = csv.DictReader(handle)

        for row in reader:
            local_code = str(row.get("local_code") or "").strip().upper()
            reason = str(row.get("reason") or "").strip()

            if local_code:
                excluded[local_code] = reason or "Excluded AU instrument"

    return excluded


AU_EXCLUDED_INSTRUMENTS = load_au_excluded_instruments()
