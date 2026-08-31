# HanjaDict (한자사전)

[![PyPI version](https://img.shields.io/pypi/v/hanjadict.svg)](https://pypi.org/project/hanjadict/)
[![Python Versions](https://img.shields.io/pypi/pyversions/hanjadict.svg)](https://pypi.org/project/hanjadict/)
[![License](https://img.shields.io/github/license/seyoungsong/hanjadict.svg)](https://github.com/seyoungsong/hanjadict/blob/master/LICENSE)
[![Downloads](https://static.pepy.tech/badge/hanjadict)](https://pepy.tech/project/hanjadict)

A lightweight Python package for looking up Hanja (Chinese characters used in Korea) information, specifically focusing on 훈음 (hun-eum).

## Installation

```sh
pip install hanjadict
```

## Usage

```py
import hanjadict

# Look up a Hanja character
result = hanjadict.lookup("雪")
print(result)
# Output: '눈 설'

# Check if a character is Hanja
is_hanja = hanjadict.is_hanja("雪")
print(is_hanja)
# Output: True

# Get only the pronunciation (음/音) part
pron = hanjadict.pronunciation("雪")
print(pron)
# Output: '설'

# Access the raw dictionary data (a plain dict: character -> 훈음)
raw_data = hanjadict.table_data
print(len(raw_data))

# If the character is not found, returns None
result = hanjadict.lookup("xyz")
print(result)  # Output: None
```

## Dictionary data

**This package does not ship dictionary data.** Only the lookup code is
distributed; you supply your own `table.json`, a UTF-8 JSON object mapping a
single Hanja character to its 훈음 string:

```json
{
  "雪": "눈 설",
  "山": "메 산",
  "燕": "제비 연/잔치 연"
}
```

`hanjadict` looks for the data in this order:

1. The path in the `HANJADICT_TABLE` environment variable
2. `table.json` inside the installed `hanjadict` package directory

If neither is found, `table_data` is an empty dict and every lookup returns
`None` / `False`.

Sources you can legally redistribute and convert into this format include
Unicode's [Unihan database](https://www.unicode.org/reports/tr38/) (`kHangul`,
Unicode License) and [libhangul](https://github.com/libhangul/libhangul)'s
`hanja.txt` (LGPL). Check each source's license before redistributing a
`table.json` built from it.

## Features

- Simple API with intuitive functions
- Lightweight with no external dependencies
- Bring-your-own dictionary data (see above)
- Access to raw dictionary data for advanced usage

## Available Functions

- `lookup(c)`: Get the full 훈음 information for a character
- `is_hanja(c)`: Check if a character is a valid Hanja in the dictionary
- `pronunciation(c)`: Extract only the Sino-Korean pronunciation (음/音) part
- `table_data`: Access the raw dictionary data (as a Python dictionary)

## What is 훈음 (Hun-eum)?

훈음 (訓音) refers to the combined Korean native word meaning (훈/訓) and Sino-Korean pronunciation (음/音) of a Hanja character. For example:

- 雪 (눈 설): "눈" is the 훈 (native Korean word for "snow") and "설" is the 음 (Sino-Korean pronunciation)
- 山 (메 산): "메" is the 훈 (native Korean word for "mountain") and "산" is the 음

This concept is unique to Korean language and helps learners understand both the meaning and pronunciation of Hanja characters.

## Special Formats Handled

The `pronunciation()` function can handle various dictionary formats:

- Normal format: "눈 설" → returns "설"
- Comma-separated: "샘솟을 집, 샘솟을 설" → returns "집"
- Slash-separated: "제비 연/잔치 연" → returns "연"
- Parentheses: "영양 령(영)" → returns "령"

## License

The MIT License in this repository applies **only to the source code**. No
license is granted to any third-party dictionary content or data. Any
`table.json` you use with this package is governed by the license of its own
source.
