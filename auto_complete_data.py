from dataclasses import dataclass


@dataclass
class AutoCompleteData:
    """
    completed_sentence: str
    source_text: str
    offset: int
    score: int
    """

    def __init__(self, completed_sentence, source_text, score, offset):
        self.completed_sentence = completed_sentence
        self.source_text = source_text
        self.score = score
        self.offset = offset
