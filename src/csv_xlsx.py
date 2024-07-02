import csv
from typing import Any

import pandas as pd


def read_csv(file_path: str) -> Any:
    poos = []
    with open(file_path, encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            poos.append(row)
    return poos


def read_xlsx(file_path: str) -> Any:
    """
    Считывает финансовые операции из XLSX-файла.
    """
    df = pd.read_excel(file_path)
    return df.to_dict("records")


# print(read_csv("../data/transactions.csv"))
# print(read_xlsx("../data/transactions_excel.xlsx"))
