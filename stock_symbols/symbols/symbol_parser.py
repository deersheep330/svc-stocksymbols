from abc import ABC

from ..db import create_engine, start_session, upsert
from ..models import Stock

class SymbolParser(ABC):

    def __init__(self):
        self.dict = None

    def parse(self):
        pass

    def get_dict(self):
        return self.dict

    def update_db(self):

        if self.dict is None:
            return self
        else:

            rows = []
            for key, value in self.dict.items():
                rows.append([key, value])

            engine = create_engine('postgres', 'admin', 'localhost', '5432', 'postgres')
            session = start_session(engine)

            upsert(session, Stock, rows)

            session.commit()
            session.close()
            return self
