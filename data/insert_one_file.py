import json

with open("data.json", "w") as data_file:
    data_dict = {}
    with open("contents.txt") as source_file:
        sentences_list = source_file.read().split("\n")
        sentences_list = list(filter(None, (line for line in sentences_list)))
        for i, sentence in enumerate(sentences_list):
            data_dict[i] = sentence
        json.dump(data_dict, data_file)

trie = {}
for i, s in data_dict.items():
    insert(i, s)

