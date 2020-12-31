from dataclasses import dataclass


@dataclass
class AutoCompleteData:
    """
    Save the user's input and the sentence
    that suits him with the score and offset.
    """
    completed_sentence: str
    source_text: str
    offset: int
    score: int
