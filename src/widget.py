from datetime import datetime


def get_mask_card_number(number: str) -> str:
    """
    Возвращает замаскированный номер для карт (формат: XXXX XX** **** XXXX).
    """
    number = str(number).replace(" ", "")

    if not number.isdigit():
        raise ValueError("Номер карты должен содержать только цифры.")
    if len(number) != 16:
        raise ValueError(f"Номер карты должен быть длиной 16 символов, получено: {len(number)}")

    masked = number[:6] + "*" * 6 + number[-4:]
    blocks = [masked[i:i+4] for i in range(0, len(masked), 4)]
    return " ".join(blocks)


def get_mask_account_number(number: str) -> str:
    """
    Возвращает замаскированный номер счёта (формат: **XXXX).
    """
    number = str(number).replace(" ", "")

    if not number.isdigit():
        raise ValueError("Номер счёта должен содержать только цифры.")

    if len(number) < 4:
        return number

    return "**" + number[-4:]


def mask_account_card(info: str) -> str:
    """
    Главная функция: принимает строку,
    извлекает номер с конца, определяет тип по длине и применяет нужную маску.
    """
    i = len(info) - 1
    while i >= 0 and info[i].isdigit():
        i -= 1

    start_of_number = i + 1
    raw_number = info[start_of_number:]

    if not raw_number:
        return info

    prefix = info[:start_of_number].strip()

    # Считаем карты строго 16-значными, всё остальное — счета
    if len(raw_number) == 16:
        masked_number = get_mask_card_number(raw_number)
    else:
        masked_number = get_mask_account_number(raw_number)

    if prefix:
        return f"{prefix} {masked_number}"
    return masked_number


def get_date(date_str: str) -> str:
    """
    Преобразует строку даты из ISO-формата в ДД.ММ.ГГГГ.
    Поддерживает микросекунды.
    """
    dt = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    return dt.strftime("%d.%m.%Y")


if __name__ == "__main__":
    # Тесты маскирования
    tests = [
        "Maestro 1596837868705199",
        "Счет 64686473678894779589",
        "MasterCard 7158300734726758",
        "Счет 35383033474447895560",
        "Visa Classic 6831982476737658",
        "Visa Platinum 8990922113665229",
        "Visa Gold 5999414228426353",
        "Счет 73654108430135874305",
    ]

    print("--- Маскирование номеров ---")
    for t in tests:
        print(f"{t!r} -> {mask_account_card(t)}")

    # Тест даты
    print("\n--- Преобразование даты ---")
    print(get_date("2024-03-11T02:26:18.671407"))
