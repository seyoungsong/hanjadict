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

# If the character is not found, returns None
result = hanjadict.lookup("xyz")
print(result)  # Output: None
```

## Features

- Fast lookups using a pre-compiled [dictionary](./src/hanjadict/table.json)
- Simple API with a single function
- Comprehensive dictionary of 53,458 characters
- Lightweight with no external dependencies

## What is 훈음 (Hun-eum)?

훈음 (訓音) refers to the combined Korean native word meaning (훈/訓) and Sino-Korean pronunciation (음/音) of a Hanja character. For example:

- 雪 (눈 설): "눈" is the 훈 (native Korean word for "snow") and "설" is the 음 (Sino-Korean pronunciation)
- 山 (메 산): "메" is the 훈 (native Korean word for "mountain") and "산" is the 음

This concept is unique to Korean language and helps learners understand both the meaning and pronunciation of Hanja characters.
