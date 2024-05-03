import pytest

from src.widget import data_split, mask_of_card_number_and_bill_number


@pytest.fixture
def input_number() -> str:
    return "Visa Platinum 7000792289606361"


def test_mask_of_card_number_and_bill_number(input_number: str) -> None:
    assert mask_of_card_number_and_bill_number(input_number) == "Visa Platinum 7000 79** **** 6361"


@pytest.fixture
def input_data() -> str:
    return "2018-07-11T02:26:18.671407"


def test_data_split(input_data: str) -> None:
    assert data_split(input_data) == "11.07.2018"
