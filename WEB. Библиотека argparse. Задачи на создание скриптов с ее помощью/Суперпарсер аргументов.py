import argparse
import sys
parser = argparse.ArgumentParser()
parser.add_argument('arg', metavar='arg', nargs='*',
                    type=str)
args = parser.parse_args()
if len(args.arg) > 0:
    print('\n'.join(i for i in args.arg))
else:
    print('no args')