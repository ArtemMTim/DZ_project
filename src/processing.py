from typing import List
from datetime import datetime


def state_func(dict_list: List[dict], state: str = "EXECUTED") -> List[dict]:
    """Функция принимает список словарей и занчение ключа 'state' по-умолчанию равного 'EXECUTED'.
    Вщзвращает список словарей с ключом 'state' равным заданному значению"""
    return [dictionary for dictionary in dict_list if dictionary.get("state") == state]


lst = [{"a": 1, "state": 2}, {"a": 2, "state": 2}, {"a": 3, "state": 2}]
print(state_func(lst, 2))


def date_sort_func(dict_list: List[dict], direction: bool = True) -> List[dict]:
    """Функция принимает список словарей и необязательное значение направления сортировки - возрастание либо убывание.
    По-умолчанию необязательный параметр равен 'False' - убывание.
    Возвращает отсортированный  согласно направлению сортировки список словарей."""
    return sorted(dict_list, key=lambda x: datetime.fromisoformat(x.get("date")), reverse=direction)


test_list = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
print(date_sort_func(test_list))
