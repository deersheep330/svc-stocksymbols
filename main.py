from stocksymbols.db import create_engine, start_session
from stocksymbols.models import Stock
from fastapi import FastAPI

engine = create_engine('mysql+pymysql', 'root', 'admin', 'db', '3306', 'mydb')
#engine = create_engine('postgres', 'admin', 'db', '5432', 'postgres')

app = FastAPI()

@app.get("/stocks")
async def get_stocks_all():
    try:
        session = start_session(engine)
        res = session.query(Stock).all()
    except Exception as e:
        print(e)
        res = e
    finally:
        session.close()
        return res

@app.get("/stocks/{symbol}")
async def get_stock_by_symbol(symbol: str = None):
    try:
        session = start_session(engine)
        res = session.query(Stock).filter_by(symbol=symbol).first()
    except Exception as e:
        print(e)
        res = e
    finally:
        session.close()
        return res
