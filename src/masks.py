def get_mask_card_number(number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску."""
    number = str(number).replace(" ", "")
    masked = number[:6] + "*" * 6 + number[-4:]
    blocks = [masked[i : i + 4] for i in range(0, len(masked), 4)]

    return " ".join(blocks)


def get_mask_account(number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску."""
    return "*" * (len(number[-6:-4])) + number[-4:]


print(get_mask_card_number("7000792289606361"))
print(get_mask_account("73654108430135874305"))
