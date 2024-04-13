from src.masks import mask_for_bill_number, mask_for_number_card

print(mask_for_number_card(input("Введите номер карты:")))
print(mask_for_bill_number(input("Введите номер счёта:")))

