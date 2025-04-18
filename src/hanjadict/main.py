from typing import Optional

from hanjadict.table import table_data


def lookup(c: str) -> Optional[str]:
    return table_data.get(c, None)


def is_hanja(c: str) -> bool:
    return c in table_data


def pronunciation(ch: str) -> Optional[str]:
    hun_eum = lookup(ch)
    if hun_eum is None:
        return None

    # Handle different formats
    # For entries with slash: "제비 연/잔치 연" -> "연"
    if "/" in hun_eum:
        # Get the first pronunciation after the slash
        parts = hun_eum.split("/")
        first_part = parts[0].strip()
        words = first_part.split()
        if len(words) > 1:
            return words[-1]
        else:
            # Handle edge cases where format is different
            return parts[0].strip()

    # For normal entries: "눈 설" -> "설"
    words = hun_eum.split()
    if len(words) >= 2:
        # The last word is usually the pronunciation
        return words[-1]

    # For entries with parentheses: "영양 령(영)" -> "령"
    if "(" in hun_eum:
        words = hun_eum.split()
        for word in words:
            if "(" in word:
                return word.split("(")[0]

    # If we can't determine the pronunciation, return the whole string
    return hun_eum


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
