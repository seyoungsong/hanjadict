import json
from pathlib import Path


def load_table(filename: Path) -> dict:
    table: dict = json.loads(Path(filename).read_text(encoding="utf-8"))
    return table


basepath = Path(__file__).parent.absolute()
table_data = load_table(basepath / "table.json")
table_data.__doc__ = """
Dictionary containing Hanja characters as keys and their 훈음 (Hun-eum) information as values.

The dictionary is loaded from the pre-compiled table.json file.

Each key is a single Hanja character and each value is a string in the format "훈 음",
where "훈" is the native Korean meaning and "음" is the Sino-Korean pronunciation.

Examples:
    >>> table_data["雪"]
    '눈 설'
    >>> table_data["山"]
    '메 산'
"""
