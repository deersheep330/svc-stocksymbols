from stock_symbols.symbols import Sp500Parser

if __name__ == '__main__':

    print('==> start')

    sp500 = Sp500Parser().parse().get_dict()

    print(sp500)