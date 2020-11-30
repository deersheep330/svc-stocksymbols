from stocksymbols.db import create_engine, start_session
from stocksymbols.models import Stock
from fastapi import FastAPI

engine = create_engine('postgres', 'admin', 'localhost', '5432', 'postgres')
session = start_session(engine)

app = FastAPI()

@app.get("/stocks")
async def get_stocks_all():
    res = session.query(Stock).all()
    return res

@app.get("/stocks/{symbol}")
async def get_stock_by_symbol(symbol: str = None):
    res = session.query(Stock).filter_by(symbol=symbol).first()
    return res
