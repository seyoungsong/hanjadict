from src import hanjadict


def test_all_pronunciations():
    """Test pronunciation extraction for all characters in table_data."""
    failures = []

    for char, hun_eum in hanjadict.table_data.items():
        pron = hanjadict.pronunciation(char)

        # Check that pronunciation is not None
        if pron is None:
            failures.append(
                f"Character '{char}' ({hun_eum}) returned None for pronunciation"
            )
            continue

        # Basic validation: pronunciation should be at least 1 character
        if len(pron) < 1:
            failures.append(
                f"Character '{char}' ({hun_eum}) returned empty pronunciation: '{pron}'"
            )
            continue

        # Check that pronunciation is actually the last character in the hun_eum
        # (after handling special formats)

        # Handle comma-separated entries
        processed_hun_eum = hun_eum
        if "," in processed_hun_eum:
            processed_hun_eum = processed_hun_eum.split(",")[0].strip()

        # Handle slash-separated entries
        if "/" in processed_hun_eum:
            processed_hun_eum = processed_hun_eum.split("/")[0].strip()

        # Handle parentheses
        if "(" in processed_hun_eum:
            processed_hun_eum = processed_hun_eum.split("(")[0].strip()

        expected_pron = processed_hun_eum[-1] if processed_hun_eum else None

        if pron != expected_pron:
            failures.append(
                f"Character '{char}' ({hun_eum}): expected '{expected_pron}', got '{pron}'"
            )

    # If there are any failures, fail the test with details
    assert not failures, (
        f"Pronunciation failures ({len(failures)}):\n"
        + "\n".join(failures[:20])
        + (
            f"\n... and {len(failures) - 20} more failures"
            if len(failures) > 20
            else ""
        )
    )


def test_lookup_valid_character():
    """Test lookup with valid Hanja character."""
    result = hanjadict.lookup("雪")
    assert result == "눈 설"


def test_lookup_another_valid_character():
    """Test lookup with another valid character."""
    result = hanjadict.lookup("山")
    assert result == "메 산"  # Replace with actual expected result


def test_lookup_invalid_character():
    """Test lookup with invalid character."""
    result = hanjadict.lookup("xyz")
    assert result is None


def test_lookup_empty_string():
    """Test lookup with empty string."""
    result = hanjadict.lookup("")
    assert result is None


def test_is_hanja_valid_character():
    """Test is_hanja with valid Hanja character."""
    assert hanjadict.is_hanja("雪") is True
    assert hanjadict.is_hanja("山") is True


def test_is_hanja_invalid_character():
    """Test is_hanja with invalid character."""
    assert hanjadict.is_hanja("xyz") is False
    assert hanjadict.is_hanja("") is False
    assert hanjadict.is_hanja("한글") is False


def test_pronunciation_normal_format():
    """Test pronunciation with normal format 'meaning pronunciation'."""
    assert hanjadict.pronunciation("雪") == "설"  # 눈 설
    assert hanjadict.pronunciation("山") == "산"  # 메 산


def test_pronunciation_with_parentheses():
    """Test pronunciation with parentheses format."""
    assert hanjadict.pronunciation("䴫") == "령"  # 영양 령(영)


def test_pronunciation_with_slash():
    """Test pronunciation with slash format."""
    assert hanjadict.pronunciation("燕") == "연"  # 제비 연/잔치 연


def test_pronunciation_with_comma():
    """Test pronunciation with comma format."""
    result = hanjadict.pronunciation("㴕")  # 샘솟을 집, 샘솟을 설
    assert (
        result == "집" or result == "설"
    )  # Either is acceptable based on implementation


def test_pronunciation_invalid_character():
    """Test pronunciation with invalid character."""
    assert hanjadict.pronunciation("xyz") is None
    assert hanjadict.pronunciation("") is None
