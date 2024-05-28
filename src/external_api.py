import requests

from src.logger import setup_logger

logger = setup_logger()


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
            logger.info("currency успешно выведено")
            return float(amount * usd_rate)
        elif currency == "EUR":
            logger.info("currency успешно выведено")
            return float(amount * eur_rate)
        else:
            logger.error("currency не выведнно")
            raise ValueError(f"Unsupported currency: {currency}")
