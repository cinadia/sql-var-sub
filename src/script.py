from sqlalchemy import create_engine
from sqlalchemy import text

ENGINE_URL = 'postgresql://postgres:postgres@localhost:5129/postgres'

engine = create_engine(ENGINE_URL)  # sqlalchemy engine

with engine.connect() as con:
    with open('substitution_builder.sql') as file:
        query = text(file.read())
        con.execute(query)