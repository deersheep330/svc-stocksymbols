from stocksymbols.db import create_engine, start_session
from stocksymbols.models import Stock

if __name__ == '__main__':

    engine = create_engine('postgres', 'admin', 'localhost', '5432', 'postgres')
    session = start_session(engine)

    res = session.query(Stock).all()
    for i in res:
        print(i)

    res = session.query(Stock).filter_by(symbol='00692').first()
    print(res)
