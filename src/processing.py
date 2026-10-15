from typing import List, Dict, Any


def filter_by_state(
    records: List[Dict[str, Any]],
    state: str = "EXECUTED"
) -> List[Dict[str, Any]]:
    """
    Возвращает новый список словарей, где значение ключа 'state' совпадает с указанным.

    :param records: список словарей с данными операций
    :param state: значение для фильтрации по ключу 'state', по умолчанию 'EXECUTED'
    :return: отфильтрованный список словарей
    """
    return [record for record in records if record.get("state") == state]


def sort_by_date(
    records: List[Dict[str, Any]],
    reverse: bool = True
) -> List[Dict[str, Any]]:
    """
    Сортирует список словарей по полю 'date' (ISO-строка) и возвращает новый список.

    Даты в формате ISO 8601 (например, '2019-07-03T18:35:29.512364') можно сортировать
    лексикографически, так как формат гарантирует корректное упорядочивание.

    :param records: список словарей с данными операций
    :param reverse: если True — сортировка по убыванию (сначала самые свежие),
                    если False — по возрастанию
    :return: отсортированный список словарей
    """
    # Для ISO-строк достаточно сортировки строк: они уже упорядочены по времени
    return sorted(records, key=lambda x: x.get("date", ""), reverse=reverse)
