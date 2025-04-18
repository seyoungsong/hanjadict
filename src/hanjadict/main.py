from typing import Optional

from hanjadict.table import table_data


def lookup(ch: str) -> Optional[str]:
    return table_data.get(ch, None)


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
    d1 = df_etc.to_dict(orient="records")
    Path("temp.json").write_text(
        json.dumps(d1, ensure_ascii=False, indent=2), encoding="utf-8"
    )
