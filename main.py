from stock_symbols.symbols import Sp500Parser, DowJonesParser, NasdaqParser, SoxParser, TWSEParser
from pprint import pprint
from stock_symbols.db import create_engine, start_session
from stock_symbols.models import Stock

if __name__ == '__main__':

    engine = create_engine('postgres', 'admin', 'localhost', '5432', 'postgres')
    session = start_session(engine)
    '''
    res = session.query(Stock).all()
    for i in res:
        print(i)
    '''
    res = session.query(Stock).filter_by(symbol='00692').first()
    print(res)

'''
    print('==> start')

    sp500 = Sp500Parser().parse().update_db().get_dict()

    pprint(sp500)

    dowjones = DowJonesParser().parse().update_db().get_dict()

    pprint(dowjones)

    nasdaq = NasdaqParser().parse().update_db().get_dict()

    pprint(nasdaq)

    sox = SoxParser().parse().update_db().get_dict()

    pprint(sox)

    twse = TWSEParser().parse().update_db().get_dict()

    pprint(twse)
'''
