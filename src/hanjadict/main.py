from typing import Optional

from hanjadict.table import table_data


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
        hun_eum = hun_eum.split("(")[0].split()

    return hun_eum[-1] if hun_eum else None


def __dev__():
    import json
    from pathlib import Path

    import pandas as pd

    df = pd.DataFrame(table_data.items(), columns=["hj", "ko"])

    df1 = df[df["ko"].str.contains(",")].reset_index(drop=True)
    df2 = df[df["ko"].str.contains(r"\(")].reset_index(drop=True)
    df3 = df[df["ko"].str.contains(r"\/")].reset_index(drop=True)

    idx = df["hj"].isin(df1["hj"]) | df["hj"].isin(df2["hj"]) | df["hj"].isin(df3["hj"])
    df_etc = df[~idx].reset_index(drop=True)
    df_hmm = df[idx].reset_index(drop=True)

    df_sample = pd.concat([df_etc.sample(10), df_hmm.sample(40)]).reset_index(drop=True)
    df_sample.sort_values("hj", inplace=True)
    d1 = df_sample.set_index("hj")["ko"].to_dict()
    Path("temp.json").write_text(
        json.dumps(d1, ensure_ascii=False, indent=2), encoding="utf-8"
    )
