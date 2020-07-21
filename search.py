import string

from auto_complete_data import AutoCompleteData

data = {1: "a y", 2: "asd"}

trie = {"a": {" ": {"y": {"$": [{"id": 1, "score": 3, "offset": 7}]}, "$": [{"id": 1, "score": 3, "offset": 7}]},
              "s": {"d": {"$": [2]}, "$": [2]},
              "$": [1, 2]}}


def fix_sentence(sentence):
    s = sentence[:]
    s.translate(str.maketrans('', '', string.punctuation))
    " ".join(s.split(" "))  # TODO
    return s.lower()


def create_auto_complete(search_input, completion_list):
    objects_completion_list = []

    for completion in completion_list:
        objects_completion_list.append(
            AutoCompleteData(data[completion["id"]],
                             search_input, completion["score"],
                             completion["offset"]))

    return objects_completion_list


def get_best_completions(search_input):
    global trie
    curr = trie
    for letter in fix_sentence(search_input):
        curr = curr[letter]

    return create_auto_complete(search_input, curr["$"])


print(get_best_completions("a y")[0].score)
