from stock_symbols.symbols import Sp500Parser, DowJonesParser, NasdaqParser, SoxParser, TWSEParser
from pprint import pprint

if __name__ == '__main__':

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