from sqlalchemy import create_engine
from sqlalchemy import text
import psycopg2
# or from sqlalchemy.sql import text

ENGINE_URL = 'postgresql://postgres:postgres@localhost:5129/postgres'

engine = create_engine(ENGINE_URL)  # sqlalchemy engine

# conn = psycopg2.connect( # psycopg2 connection
#     host="localhost",
#     database="postgres",
#     user="postgres",
#     password="ccuipostgresql",
#     port="5129")
# conn.set_session(autocommit=False)

with engine.connect() as con:
    with open('substitution_builder.sql') as file:
        query = text(file.read())
        con.execute(query)