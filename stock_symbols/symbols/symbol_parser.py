from abc import ABC

class SymbolParser(ABC):

    def __init__(self):
        self.dict = None

    def parse(self):
        pass

    def get_dict(self):
        return self.dict
