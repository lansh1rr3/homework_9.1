import json
from typing import Any, Dict

from src.external_api import get_currency_rate
from src.logger import setup_logger

logger = setup_logger()


def load_operations(file_path: str) -> list[dict]:
    """
    Функция загружает данные о финансовых транзакциях из JSON-файла.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                logger.info("Всё отлично")
                return data
            else:
                logger.error("Ошибка")
                return []
    except FileNotFoundError:
        logger.error("Файл не найден")
        return []


def sum_amount(transaction: Dict[str, Any]) -> float:
    """Возвращает сумму транзакции в рублях."""
    total = 0.0
    operation_sum = transaction.get("operationAmount", {})
    currency_code = operation_sum.get("currency", {}).get("code", "")
    amount = float(operation_sum.get("amount", 0.0))
    if currency_code in ["USD", "EUR"]:
        rate_to_rub = get_currency_rate(currency_code)
        total += amount * rate_to_rub
    elif currency_code == "RUB":
        total += amount
        logger.info("Function sum_amount completed successfully")
        return total
    else:
        logger.error("Something went wrong with the sum_amount function: %(error)s")
    return total


value = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589",
}

# convert_amount(value)
