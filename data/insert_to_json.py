import json
import os


def go_on_files():
    list_of_files = list()
    for (dir_path, dir_names, file_names) in os.walk("technology_texts"):
        list_of_files += [os.path.join(dir_path, file) for file in file_names]

    for file in list_of_files:
        data_dict = {}
        with open(file, encoding="utf8") as the_file:
            sentences = the_file.read().split("\n")
        for index, sentence in enumerate(sentences):
            data_dict[index] = sentence

    with open("data.json", "w") as data_file:
        json.dump(data_dict, data_file)

    return data_dict
