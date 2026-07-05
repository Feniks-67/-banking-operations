def get_mask_card_number(number: str) -> str:
    """Функция, которая возвращает замаскированный номер для карт"""
    number = str(number).replace(" ", "")
    masked = number[:6] + "*" * 6 + number[-4:]
    blocks = [masked[i:i+4] for i in range(0, len(masked), 4)]
    return " ".join(blocks)


def get_mask_account_number(number: str) -> str:
    """Функция, которая возвращает замаскированный номер для счетов"""
    number = str(number).replace(" ", "")
    if len(number) < 4:
        return number
    return "**" + number[-4:]


def mask_account_card(info: str) -> str:
    """Главная функция: принимает строку и определяет тип по длине
    найденного номера и применяет нужную маску."""
    i = len(info) - 1
    while i >= 0 and info[i].isdigit():
        i -= 1

    start_of_number = i + 1
    raw_number = info[start_of_number:]

    if not raw_number:
        return info

    prefix = info[:start_of_number].strip()

    if len(raw_number) == 16:
        masked_number = get_mask_card_number(raw_number)
    else:
        masked_number = get_mask_account_number(raw_number)

    if prefix:
        return f"{prefix} {masked_number}"
    return masked_number


# Тестовые данные
tests = [
"Maestro 1596837868705199",
"Счет 64686473678894779589",
"MasterCard 7158300734726758",
"Счет 35383033474447895560",
"Visa Classic 6831982476737658",
"Visa Platinum 8990922113665229",
"Visa Gold 5999414228426353",
"Счет 73654108430135874305"
    ]

for t in tests:
    print(mask_account_card(t))


def get_date(date_str: str) -> str:
    """Преобразует строку даты в формат ДД.ММ.ГГГГ."""
    dt = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    return dt.strftime("%d.%m.%Y")


# Тестовые данные
print(get_date("2024-03-11T02:26:18.671407"))

