def mask_for_number_card(card_number: str) -> str:
    """
    Данная функция скрывает часть номера карта
    символом *, и возвращает замаскированную версию
    """
    mask_card = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return mask_card


def mask_for_bill_number(bill_number: str) -> str:
    """
    Данная функция скрывает большую часть двумя
    символами * и оставляет в конце 4 последних цифры
    """
    number_bill = f"**{bill_number[-4:]}"
    return number_bill
