from stock_symbols.symbols import Sp500Parser, DowJonesParser, NasdaqParser, SoxParser, TWSEParser
from pprint import pprint
import sqlalchemy
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy import create_engine


def connect(user='postgres', password='admin', db='postgres', host='localhost', port=5432):

    url = f'postgresql://{user}:{password}@{host}:{port}/{db}'

    con = sqlalchemy.create_engine(url, client_encoding='utf8')
    meta = sqlalchemy.MetaData()
    meta.reflect(con)

    return con, meta

def insert_into_db(conn, meta):
    stock = meta.tables['stock']
    stmt = insert(stock).values(symbol='T', name='United Kingdom')
    update_stmt = stmt.on_conflict_do_update(
        index_elements=[stock.c.symbol],
        set_=dict(name='Dup')
    )
    result = conn.execute(update_stmt)
    print(result)


if __name__ == '__main__':

    engine = create_engine('postgresql://postgres:admin@localhost:5432/postgres')
    conn = engine.connect()
    conn.execute("INSERT INTO stock VALUES ('T', 'john')")  # autocommits

'''
    con, meta = connect()
    print(con)
    print(meta.tables.keys())
    meta.tables
    insert_into_db(con, meta)
'''

'''
    print('==> start')

    sp500 = Sp500Parser().parse().get_dict()

    pprint(sp500)

    dowjones = DowJonesParser().parse().get_dict()

    pprint(dowjones)

    nasdaq = NasdaqParser().parse().get_dict()

    pprint(nasdaq)

    sox = SoxParser().parse().get_dict()

    pprint(sox)

    twse = TWSEParser().parse().get_dict()

    pprint(twse)
'''