import json
import string
import re
from auto_complete_data import AutoCompleteData

data_dict = {}
search_dict = {}


def open_files():
    with open("data/data.json") as data_file:
        global data_dict
        data_dict = json.load(data_file)

    with open("data/search_file.json") as search_file:
        global search_dict
        search_dict = json.load(search_file)


def fix_sentence(sentence):
    s = sentence[:]
    s.translate(str.maketrans('', '', string.punctuation))
    s = re.sub(' +', ' ', s)
    return s.lower()


def create_auto_complete(completion_list, search_input):
    object_completion_list = []
    for completion in completion_list:
        object_completion_list.append(AutoCompleteData(
            data_dict[str(completion["id"])],
            search_input, completion["score"],
            completion["offset"]))

    return object_completion_list


def get_best_completions(search_input):
    fix_input = fix_sentence(search_input)[:5]
    if not search_dict.get(fix_input):
        return []
    return create_auto_complete(
        search_dict[fix_sentence(fix_input)],
                                search_input)
