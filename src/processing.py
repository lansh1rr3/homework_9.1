from datetime import datetime
from typing import Dict, List


def filter_by_state(data: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    функция, которая фильтрует список словарей
    """
    return [item for item in data if item["state"] == state]


def sort_by_date(data: List[Dict], reverse: bool = True) -> List[Dict]:
    def sort_key(item: Dict) -> datetime:
        """
        функция, которая фильтрует список словарей по дате
        """
        return datetime.strptime(item["date"], "%Y-%m-%dT%H:%M:%S.%f")

    return sorted(data, key=sort_key, reverse=reverse)
