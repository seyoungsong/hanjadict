import json
import os
from pathlib import Path


def load_table(filename: Path) -> dict:
    table: dict = json.loads(Path(filename).read_text(encoding="utf-8"))
    return table


def _find_table() -> "Path | None":
    """
    Locate the dictionary data file.

    The dictionary data is NOT bundled with this package. Resolution order:
      1. HANJADICT_TABLE environment variable (path to a JSON file)
      2. table.json next to this module
    """
    env = os.environ.get("HANJADICT_TABLE")
    if env:
        return Path(env)
    local = Path(__file__).parent.absolute() / "table.json"
    if local.is_file():
        return local
    return None


_table_path = _find_table()
table_data: dict = load_table(_table_path) if _table_path else {}
