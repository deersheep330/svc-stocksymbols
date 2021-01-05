from symbols.symbols import Sp500Parser, DowJonesParser, NasdaqParser, SoxParser, TWSEParser, NYSEParser
from pprint import pprint

if __name__ == '__main__':

    print('==> update start')

    nyse = NYSEParser().parse().dump_to_file().update_db().get_dict()

    #pprint(nyse)

    sp500 = Sp500Parser().parse().dump_to_file().update_db().get_dict()

    #pprint(sp500)

    dowjones = DowJonesParser().dump_to_file().parse().update_db().get_dict()

    #pprint(dowjones)

    nasdaq = NasdaqParser().parse().dump_to_file().update_db().get_dict()

    #pprint(nasdaq)

    sox = SoxParser().parse().dump_to_file().update_db().get_dict()

    #pprint(sox)

    twse = TWSEParser().parse().dump_to_file().update_db().get_dict()

    #pprint(twse)

    print('==> update done')
