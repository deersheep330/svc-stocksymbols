from .symbol_parser import SymbolParser
import requests
from lxml import etree
from ..utils import remove_common_words_from_corp_name

class Sp500Parser(SymbolParser):

    def __init__(self):
        self.url = 'https://www.cnyes.com/usastock/hotprice.aspx?page=hot&kind=sp500'
        super(Sp500Parser, self).__init__()
        print(f'==> s&p 500 parser init')

    def parse(self):
        print(f'==> parse page: {self.url}')
        resp = requests.get(self.url)
        content = resp.text
        tree = etree.HTML(content)

        symbols = tree.xpath("//table[contains(@id, 'stock')]//tr/td[2]/a")
        names = tree.xpath("//table[contains(@id, 'stock')]//tr/td[3]/a")
        self.dict = {}
        for symbol, name in zip(symbols, names):
            _symbol = symbol.text
            _name = remove_common_words_from_corp_name(name.text)
            self.dict[_symbol] = _name

        print(f'==> get {len(self.dict)} symbols')

        return self
