def make_trie(*words):
    root = dict()
    for word in words:
        current_dict = root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict.setdefault("$", [])
        current_dict["$"].append(word)
    return root


print(make_trie(["as", "a", "ad"]))
