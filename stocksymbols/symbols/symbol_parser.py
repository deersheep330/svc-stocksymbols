import json
from abc import ABC
import os

from ..db import create_engine, start_session, upsert
from ..models import Stock

class SymbolParser(ABC):

    def __init__(self):
        self.dict = None

    def parse(self):
        pass

    def get_dict(self):
        return self.dict

    def dump_to_file(self):

        if self.dict is None or len(self.dict) == 0:
            pass
        else:

            print(f'==> dump to file')

            filename = './stocksymbols/dump/' + self.filename
            os.makedirs(os.path.dirname(filename), exist_ok=True)

            with open(filename, 'w+', encoding='utf-8') as f:
                json.dump(self.dict, f, ensure_ascii=False, indent=4)

        return self

    def update_db(self):

        if self.dict is None or len(self.dict) == 0:
            pass
        else:

            print(f'==> update db')

            rows = []
            for key, value in self.dict.items():
                rows.append([key, value])

            engine = create_engine('mysql+pymysql', 'root', 'admin', 'db', '3306', 'mydb')
            #engine = create_engine('postgresql', 'postgres', 'admin', 'db', '5432', 'postgres')
            session = start_session(engine)

            upsert(session, Stock, rows)

            session.commit()
            session.close()

        return self
