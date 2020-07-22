import json
from string import ascii_lowercase

with open("data.json", "w") as data_file:
    data_dict = {}
    with open("contents.txt") as source_file:
        sentences_list = source_file.read().split("\n")
        sentences_list = list(filter(None, (line for line in sentences_list)))
        for i, sentence in enumerate(sentences_list):
            data_dict[i] = sentence
        json.dump(data_dict, data_file)


def insert(d, id_, s, score, offset):
    if s not in d.keys():
        d[s] = [{"id": id_, "score": score, "offset": offset}]
    else:
        for index in range(len(d[s])):
            flag = False
            if d[s][index]["id"] == id_:
                flag = True
                if d[s][index]["score"] < score:
                    d[s].pop(index)
                    flag = False
                    break
        if not flag:
            d[s].append({"id": id_, "score": score, "offset": offset})
            d[s].sort(key=lambda x: x["score"])
            d[s] = d[s][:5]


def insert_with_delete(d, id_, s, index, offset):
    s_delete = s[:index] + s[index + 1:] if index + 1 < len(s) else s[:index]
    score = (2 * len(s) - (10 - 2 * index)) if index < 4 else (2 * len(s) - 2)

    insert(d, id_, s_delete, score, offset)


def insert_with_add(d, id_, s, index, letter, offset):  # TODO: in last place?
    s_add = s[:index] + letter + s[index:]
    score = (2 * len(s) - (10 - 2 * index)) if index < 4 else (2 * len(s) - 2)
    insert(d, id_, s_add, score, offset)


def insert_with_replace(d, id_, s, index, letter, offset):
    if letter == s[index]:
        s_replace = s[:index] + letter + s[index + 1:] if index + 1 < len(s) else s[:index] + letter
        score = (2 * len(s) - (10 - 2 * index)) if index < 4 else (2 * len(s) - 2)
        insert(d, id_, s_replace, score, offset)
    else:
        insert(d, id_, s, 2 * len(s), offset)


def with_mistakes(d, id_, s, offset):
    for index in range(len(s)):
        insert_with_delete(d, id_, s, index, offset)
        for letter in ascii_lowercase:
            insert_with_add(d, id_, s, index, letter, offset)
            insert_with_replace(d, id_, s, index, letter, offset)


def insert_substrings(d, id_):
    for start_index in range(len(data_dict[id_])):
        for end_index in range(start_index, len(data_dict[id_])):
            with_mistakes(d, id_, data_dict[id_][start_index: end_index], start_index)


def create_dict():
    d = {}

    for id_, s in data_dict.items():
        insert_substrings(d, id_)

    with open("search_file.json", "w") as search_file:
        json.dump(d, search_file)

    print(d)


create_dict()
