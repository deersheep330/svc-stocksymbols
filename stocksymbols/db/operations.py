from sqlalchemy.dialects.mysql import insert as mysql_insert
from sqlalchemy.dialects.postgresql import insert as postgres_insert
from sqlalchemy import create_engine as __create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects import postgresql, mysql

from ..db import Base



def create_engine(adapter, user, password, host, port, database):
    create_engine.adapter = adapter
    print(f'==> create_engine for {create_engine.adapter}')
    try:
        return create_engine.engine
    except AttributeError:
        print('create new engine')
        create_engine.engine = __create_engine(f'{adapter}://{user}:{password}@{host}:{port}/{database}', pool_recycle=3600*7)
        return create_engine.engine

def create_all_tables_from_orm(engine):
    Base.metadata.create_all(engine)

def start_session(engine):
    print('==> start_session()')
    try:
        return start_session.session_maker()
    except AttributeError:
        print('create new session maker')
        start_session.session_maker = sessionmaker()
        start_session.session_maker.configure(bind=engine)
        return start_session.session_maker()

def compile_query(query):
    """from http://nicolascadou.com/blog/2014/01/printing-actual-sqlalchemy-queries"""
    compiler = query.compile if not hasattr(query, 'statement') else query.statement.compile
    if create_engine.adapter == 'mysql+pymysql':
        return compiler(dialect=mysql.dialect())
    else:
        return compiler(dialect=postgresql.dialect())

def upsert(session, model, rows):

    table = model.__table__

    if create_engine.adapter == 'mysql+pymysql':

        rowcount = 0

        for row in rows:
            data_dict = {}
            for column, value in zip(table.c, row):
                data_dict[column.name] = value
            data_dict_wo_pk = dict(data_dict)
            for pk in list(table.primary_key.columns):
                del data_dict_wo_pk[pk.name]
            stmt = mysql_insert(table).values(data_dict)
            #print(f'data_dict = {data_dict}, wo pk = {data_dict_wo_pk}')
            upsert_stmt = stmt.on_duplicate_key_update(data_dict_wo_pk)

            #print(compile_query(upsert_stmt))
            res = session.execute(upsert_stmt)
            if res.rowcount != 0:
                rowcount += 1

        print(f'{rowcount} row(s) matched')
    else:
        stmt = postgres_insert(table).values(rows)

        update_cols = [
            c.name for c in table.c if c not in list(table.primary_key.columns)
        ]

        upsert_stmt = stmt.on_conflict_do_update(
            index_elements=table.primary_key.columns,
            set_={
                k: getattr(stmt.excluded, k) for k in update_cols
            }
        )

        #print(compile_query(upsert_stmt))
        res = session.execute(upsert_stmt)
        print(f'{res.rowcount} row(s) matched')
