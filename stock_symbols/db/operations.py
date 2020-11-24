from sqlalchemy.dialects.postgresql import insert
from sqlalchemy import create_engine as __create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects import postgresql

from ..db import Base

def create_engine(user, password, host, port, database):
    engine = __create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')
    return engine

def create_all_tables_from_orm(engine):
    Base.metadata.create_all(engine)

def start_session(engine):
    try:
        return start_session.session_maker()
    except AttributeError:
        start_session.session_maker = sessionmaker()
        start_session.session_maker.configure(bind=engine)
        return start_session.session_maker()

def compile_query(query):
    """from http://nicolascadou.com/blog/2014/01/printing-actual-sqlalchemy-queries"""
    compiler = query.compile if not hasattr(query, 'statement') else query.statement.compile
    return compiler(dialect=postgresql.dialect())

def upsert(session, model, rows):

    table = model.__table__
    stmt = insert(table).values(rows)

    update_cols = [
        c.name for c in table.c if c not in list(table.primary_key.columns)
    ]

    on_conflict_stmt = stmt.on_conflict_do_update(
        index_elements=table.primary_key.columns,
        set_={
            k: getattr(stmt.excluded, k) for k in update_cols
        }
    )

    #print(compile_query(on_conflict_stmt))
    res = session.execute(on_conflict_stmt)
    print(f'{res.rowcount} row(s) matched')
