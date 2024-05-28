import json

import requests

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


def convert_amount(operation: dict) -> float:
    """
    Функция конвертирует сумму транзакции в рубли.
    """
    amount = operation["operationAmount"]["amount"]
    currency = operation["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return float(amount)
    else:
        url = "https://www.cbr-xml-daily.ru/daily_json.js"
        response = requests.get(url)
        data = response.json()
        usd_rate = float(data["Valute"]["USD"]["Value"])
        eur_rate = float(data["Valute"]["EUR"]["Value"])

        if currency == "USD":
            logger.info("Вывело успешно")
            return float(amount * usd_rate)
        elif currency == "EUR":
            logger.info("Вывело успешно")
            return float(amount * eur_rate)
        else:
            logger.error("Не удалось конвертировать")
            raise ValueError(f"Unsupported currency: {currency}")


dict_for_test = [
    {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": 10, "currency": {"name": "USD", "code": "USD"}},
    }
]

print(load_operations("../data/operations.json"))
print(convert_amount(dict_for_test[0]))

value = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589",
}

convert_amount(value)
