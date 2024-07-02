import unittest
from typing import Any
from unittest.mock import mock_open, patch

import pandas as pd

from src.csv_xlsx import read_csv, read_xlsx


class TestReadCSV(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="Date;Description;Amount\n2022-01-01;Salary;1000\n")
    @patch("csv.DictReader")
    def test_read_csv(self, mock_csvreader: Any, mock_open: Any) -> Any:
        """
        Тестовый пример для функции read_csv.
        """
        file_path = "test.csv"
        read_csv(file_path)
        mock_open.assert_called_once_with(file_path, encoding="utf-8")
        mock_csvreader.assert_called_once()


class TestReadXLSX(unittest.TestCase):

    @patch(
        "pandas.read_excel",
        return_value=pd.DataFrame({"Date": ["2022-01-01"], "Description": ["Salary"], "Amount": [1000]}),
    )
    def test_read_xlsx(self, mock_read_excel: Any) -> None:
        """
        Тестовый пример для функции read_xlsx.
        """
        file_path = "test.xlsx"
        result = read_xlsx(file_path)
        mock_read_excel.assert_called_once_with(file_path)
        self.assertEqual(result, [{"Date": "2022-01-01", "Description": "Salary", "Amount": 1000}])


if __name__ == "__main__":
    unittest.main()
