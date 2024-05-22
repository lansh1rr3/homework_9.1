import json

import requests


def load_operations(file_path: str) -> list[dict]:
    """
    Функция загружает данные о финансовых транзакциях из JSON-файла.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                return []
    except FileNotFoundError:
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
            return float(amount * usd_rate)
        elif currency == "EUR":
            return float(amount * eur_rate)
        else:
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
