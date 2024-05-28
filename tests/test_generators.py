from src.generators import (filter_transactions_by_currency, generate_card_numbers_list,
                            get_transaction_descriptions_list, trans)

usd_transactions = filter_transactions_by_currency(trans, "USD")
descriptions = get_transaction_descriptions_list(trans)
cards = generate_card_numbers_list(1, 5)


def test_filter_transactions_by_currency() -> None:
    assert next(usd_transactions) == "939719570"
    assert next(usd_transactions) == "142264268"
    assert next(usd_transactions) == "895315941"


def test_get_transaction_descriptions_list() -> None:
    assert next(cards) == "0000000000000001"
    assert next(cards) == "0000000000000002"
    assert next(cards) == "0000000000000003"
    assert next(cards) == "0000000000000004"
    assert next(cards) == "0000000000000005"


def test_generate_card_numbers_list() -> None:
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод с карты на карту"
    assert next(descriptions) == "Перевод организации"
