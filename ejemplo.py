import argparse

parser = argparse.ArgumentParser(prog='main.py', description='Ejercicio Fibonacci')
parser.add_argument('-c', '--count')
parser.add_argument('-v', '--verbose',
                    action='store_true')
args = parser.parse_args()
print( args.count, args.verbose)
