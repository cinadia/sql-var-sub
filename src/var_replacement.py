import argparse

def var_replacement(args):
    with open(args.filename) as f:
        lines = [line.rstrip() for line in f]
        for line in lines:
            new_line = line.replace('$DB_NAME', args.DB_NAME)
            print(new_line)


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

var_replacement_parser = subparsers.add_parser('var-replace')
var_replacement_parser.add_argument('filename')
# add database name
var_replacement_parser.add_argument('--DB_NAME', default='DB')
var_replacement_parser.set_defaults(func=var_replacement)

if __name__ == '__main__':
    args = parser.parse_args()
    args.func(args)