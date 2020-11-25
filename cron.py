from stocksymbols.symbols import Sp500Parser, DowJonesParser, NasdaqParser, SoxParser, TWSEParser
from pprint import pprint

if __name__ == '__main__':

    print('==> update start')

    sp500 = Sp500Parser().parse().update_db().get_dict()

    #pprint(sp500)

    dowjones = DowJonesParser().parse().update_db().get_dict()

    #pprint(dowjones)

    nasdaq = NasdaqParser().parse().update_db().get_dict()

    #pprint(nasdaq)

    sox = SoxParser().parse().update_db().get_dict()

    #pprint(sox)

    twse = TWSEParser().parse().update_db().get_dict()

    #pprint(twse)

    print('==> update done')
