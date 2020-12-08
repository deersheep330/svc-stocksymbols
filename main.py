from stocksymbols.db import create_engine, start_session
from stocksymbols.models import Stock
from fastapi import FastAPI

engine = create_engine('mysql+pymysql', 'root', 'admin', 'db', '3306', 'mydb')
#engine = create_engine('postgres', 'admin', 'db', '5432', 'postgres')
session = start_session(engine)

app = FastAPI()

@app.get("/stocks")
async def get_stocks_all():
    try:
        res = session.query(Stock).all()
    except Exception as e:
        print(e)
        res = e
    return res

@app.get("/stocks/{symbol}")
async def get_stock_by_symbol(symbol: str = None):
    try:
        res = session.query(Stock).filter_by(symbol=symbol).first()
    except Exception as e:
        print(e)
        res = e
    return res
