import csv
from functools import lru_cache


@lru_cache
def read(path):
    with open(path, encoding="utf8") as file:
        file_to_dict = csv.DictReader(file)
        dict_to_list = list(file_to_dict)
    return dict_to_list
