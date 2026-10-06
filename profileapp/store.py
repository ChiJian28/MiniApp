"""Load the team directory from data/users.json."""

import json
from pathlib import Path


def directory_path():
    """Return the path to the synthetic directory file."""
    return Path(__file__).resolve().parents[1] / "data" / "users.json"


def load_users():
    """Return directory records keyed by integer id."""
    with directory_path().open(encoding="utf-8") as handle:
        records = json.load(handle)
    return {int(record["id"]): record for record in records}
