from src.masks import mask_for_bill_number, mask_for_number_card


def mask_of_card_number_and_bill_number(input_number: str) -> str:
    num = input_number.split()
    """Принимает на вход строку с информацией — тип карты/счета и номер карты/счета.
    Возвращает исходную строку с замаскированным номером карты/счета"""
    if "Счет" in input_number:
        mask = f"Счёт {mask_for_bill_number(num[-1])}"
    else:
        mask = f"{' '.join(input_number.split()[:-1])} {mask_for_number_card(num[-1])}"
    return mask


def data_split(data: str) -> str:
    """возвращает дату в нужном формате"""
    split_data_day_month_year = data.split("T")[0].split("-")
    return f"{split_data_day_month_year[-1]}.{split_data_day_month_year[-2]}.{split_data_day_month_year[-3]}"
