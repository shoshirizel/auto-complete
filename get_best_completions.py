import json
import string
import re

from pathlib import Path
from typing import List

from auto_complete_data import AutoCompleteData

DATA_FOLDER = Path("data")
MAX_CHARACTERS = 5


def fix_sentence(sentence: str) -> str:
    """"
    Omits punctuations and returns in small letters.
    """
    s = sentence[:]
    s.translate(str.maketrans('', '', string.punctuation))
    s = re.sub(' +', ' ', s)
    return s.lower()


class Complete:
    """"
    Gives up to 5 completions to the sentence,
    Allows one mistake, omits punctuations.
    """""
    def __init__(self):
        """
        Load data set files.
        """
        with (DATA_FOLDER / "data.json").open() as data_file:
            self.data_dict = json.load(data_file)
        with (DATA_FOLDER / "search_file.json").open() as search_file:
            self.search_dict = json.load(search_file)

    def create_auto_complete(
            self, completion_list: List[dict],
            search_input: str) -> List[AutoCompleteData]:
        """"
        Returns the end result of the sentences
        """
        object_completion_list = []
        for completion in completion_list:
            object_completion_list.append(AutoCompleteData(
                self.data_dict[str(completion["id"])],
                search_input,
                completion["score"],
                completion["offset"])
            )
        return object_completion_list

    def get_best_completions(self, search_input: str)\
            -> List[AutoCompleteData]:
        """"
        Returns list of the best completions with score and offset.
        """
        fix_input = fix_sentence(search_input)[:MAX_CHARACTERS]
        if not self.search_dict.get(fix_input):
            return []
        return self.create_auto_complete(
            self.search_dict[fix_input],
            search_input)
