from typing import Optional

from .table import table_data


def lookup(c: str) -> Optional[str]:
    return table_data.get(c, None)


def is_hanja(c: str) -> bool:
    return c in table_data


def pronunciation(c: str) -> Optional[str]:
    hun_eum = lookup(c)
    if hun_eum is None:
        return None

    # First check for entries with commas: "샘솟을 집, 샘솟을 설" -> "집"
    if "," in hun_eum:
        hun_eum = hun_eum.split(",")[0].strip()

    # For entries with slash: "제비 연/잔치 연" -> "연"
    if "/" in hun_eum:
        hun_eum = hun_eum.split("/")[0].strip()

    # For entries with parentheses: "영양 령(영)" -> "령"
    if "(" in hun_eum:
        hun_eum = hun_eum.split("(")[0].strip()

    return hun_eum[-1] if hun_eum else None
