from sqlalchemy import create_engine

filename = "test_query.sql"
# dialect[+driver]://user:password@host/dbname
#ENGINE_URL = 'postgresql://postgres:postgres@localhost:5129/postgres'
ENGINE_URL = 'postgresql://postgres:ccuipostgresql@localhost:5432/test'

engine = create_engine(ENGINE_URL)  # sqlalchemy engine


def execute_query(query):
    print("executing....")
    try:
        engine.connect().execute(query)
    except:
        raise Exception('Invalid query')


with open(filename) as f:
    lines = [line.rstrip() for line in f]

    if len(lines) == 0:
        raise Exception('Cannot parse an empty file')

    current_query = ""
    for line in lines:
        first_chars = line[0:2]
        if line != "" and first_chars != "--":
            last_char = line[-1]
            if last_char == ";":
                current_query = current_query + " " + line
                print("executed query:", current_query)
                execute_query(current_query)
                current_query = ""
            else:
                current_query = current_query + " " + line


"""
If you reach the end of the file (no more lines to read) send an error.

what if there is a ‘;’ in the middle of a line? 
"""