from src.logger import setup_logger

logger = setup_logger()


def mask_for_number_card(card_number: str) -> str:
    """
    Данная функция скрывает часть номера карта
    символом *, и возвращает замаскированную версию
    """
    if len(card_number) == 16:
        logger.info("Функция mask_for_number_card работает")
        mask_card = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        return mask_card
    else:
        logger.error("С функцией mask_for_number_card что-то не так")
    return card_number


def mask_for_bill_number(bill_number: str) -> str:
    """
    Данная функция скрывает большую часть двумя
    символами * и оставляет в конце 4 последних цифры
    """
    if len(bill_number) == 21:
        logger.info("Функция mask_for_bill_number выполнена успешно")
        number_bill = f"**{bill_number[-4:]}"
        return number_bill
    else:
        logger.error("С функцией mask_for_bill_number что-то не так")
    return bill_number


# Проверка
mask_for_number_card("9876543210123456")
mask_for_bill_number("123456789098765432112")
