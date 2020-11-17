from stock_symbols.symbols import Sp500Parser
from pprint import pprint

if __name__ == '__main__':

    print('==> start')

    sp500 = Sp500Parser().parse().get_dict()

    pprint(sp500)