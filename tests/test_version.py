from algokit_subscriber import library_info, version


def test_version_is_string() -> None:
    assert isinstance(version, str)
    assert version


def test_library_info_mentions_reference() -> None:
    assert "reference" in library_info().lower()
