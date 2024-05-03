from src.masks import mask_for_bill_number, mask_for_number_card


def test_mask_for_bill_number() -> None:
    assert mask_for_bill_number("73654108430135874305") == "**4305"


def test_mask_for_number_card() -> None:
    assert mask_for_number_card("7000792289606361") == "7000 79** **** 6361"
