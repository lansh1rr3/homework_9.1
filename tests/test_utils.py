import unittest

from requests_mock import Mocker

from src.utils import convert_amount


class TestConvertAmount(unittest.TestCase):

    def test_rub_amount(self) -> None:
        operation = {"operationAmount": {"amount": 100.00, "currency": {"code": "RUB"}}}
        self.assertEqual(convert_amount(operation), 100.00)

    def test_usd_amount(self) -> None:
        with Mocker() as mock:
            mock.get(
                "https://www.cbr-xml-daily.ru/daily_json.js",
                json={"Valute": {"USD": {"Value": 75.00}, "EUR": {"Value": 85.00}}},
            )
            operation = {"operationAmount": {"amount": 100.00, "currency": {"code": "USD"}}}
            self.assertEqual(convert_amount(operation), 7500.00)

    def test_eur_amount(self) -> None:
        with Mocker() as mock:
            mock.get(
                "https://www.cbr-xml-daily.ru/daily_json.js",
                json={"Valute": {"USD": {"Value": 75.00}, "EUR": {"Value": 85.00}}},
            )
            operation = {"operationAmount": {"amount": 100.00, "currency": {"code": "EUR"}}}
            self.assertEqual(convert_amount(operation), 8500.00)

    def test_unsupported_currency(self) -> None:
        with Mocker() as mock:
            mock.get(
                "https://www.cbr-xml-daily.ru/daily_json.js",
                json={"Valute": {"USD": {"Value": 75.00}, "EUR": {"Value": 85.00}}},
            )
            operation = {"operationAmount": {"amount": 100.00, "currency": {"code": "UAH"}}}
            with self.assertRaises(ValueError) as context:
                convert_amount(operation)
            self.assertEqual(str(context.exception), "Unsupported currency: UAH")
