from typing import TypedDict,List

class Quote(TypedDict):
    text: str
    author: str

def get_quotes() -> List[Quote]:...