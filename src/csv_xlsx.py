import csv
from typing import Any

import pandas as pd


def read_csv(file_path: str) -> Any:
    """
    Считывает финансовые операции из CSV-файла.
    """
    if file_path.endswith(".csv"):
        df = pd.read_csv(file_path, encoding="utf-8")
        transactions = df.to_dict(orient="records")
        return transactions
    else:
        return []


def read_xlsx(file_path: str) -> Any:
    """
    Считывает финансовые операции из XLSX-файла.
    """
    df = pd.read_excel(file_path)
    return df.to_dict("records")


print(read_csv("../data/transactions.csv"))
print(read_xlsx("../data/transactions_excel.xlsx"))
