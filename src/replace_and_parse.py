import argparse

import psycopg2
from sqlalchemy import create_engine
from collections import OrderedDict

# engine url format: postgresql://user:pass@localhost:5432/database

def execute_query(query, ENGINE_URL):
    engine = create_engine(ENGINE_URL)  # sqlalchemy engine
    print("executing....")
    try:
        engine.connect().execute(query)
    except psycopg2.OperationalError:
        raise Exception('Connection error.')
    except psycopg2.errors.SyntaxError:
        raise Exception('Syntax error. Check that the SQL in the file provided has correct syntax.')
    except:
        raise Exception('Invalid query.')


def replace(line, args):
    od = OrderedDict([('$DB_NAME', args.DB_NAME),
                      ('$ROLE', args.ROLE),
                      ('$PASSWORD', args.PASSWORD)])
    for i, j in od.items():
        line = line.replace(i, j)
    return line


def execute(args):
    # valid parameters, help and meaningful catch-all
    try:
        with open(args.filename) as f:
            lines = [line.rstrip() for line in f]

            #print('parsing file........')

            if len(lines) == 0:
                raise Exception('Cannot parse an empty file')

            current_query = ""
            for line in lines:
                # variable replacement
                new_line = replace(line, args)
                first_chars = new_line[0:2]
                if new_line != "" and first_chars != "--":
                    # begin parsing the line only if it isn't blank and isn't a comment
                    last_char = new_line[-1]
                    if last_char == ";":
                        current_query = current_query + " " + new_line
                        print("executed query:", current_query)
                        execute_query(current_query, args.ENGINE_URL)
                        current_query = ""
                    else:
                        current_query = current_query + " " + new_line
    except FileNotFoundError:
        print('File not found.')

# add parsers
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()
var_replacement_parser = subparsers.add_parser('var-replace')
var_replacement_parser.set_defaults(func=execute)

# add file name argument
var_replacement_parser.add_argument('--filename', help='the name of the SQL file to run')
# add engine URL argument
var_replacement_parser.add_argument('--ENGINE_URL', help='the engine URL to connect to the database')
# add database name to replace
var_replacement_parser.add_argument('--DB_NAME', default='DB', help='the name of the database to replace in the file; default: DB')
# add role name to replace
var_replacement_parser.add_argument('--ROLE', default='postgres', help='the name of the role to replace in the file; default: postgres')
# add password to replace
var_replacement_parser.add_argument('--PASSWORD', help='the password to replace in the file')


if __name__ == '__main__':
    args = parser.parse_args()
    args.func(args)
