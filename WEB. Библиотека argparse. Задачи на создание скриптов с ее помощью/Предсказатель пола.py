import argparse
dct = {
    'melodrama': 0,
    'football': 100,
    'other': 50
}
parser = argparse.ArgumentParser()
parser.add_argument('--barbie', default=50, nargs='?', type=int)
parser.add_argument('--cars', default=50, nargs='?', type=int)
parser.add_argument('--movie', default='other', nargs='?', type=str)
args = parser.parse_args()
if args.barbie not in range(0, 101):
    args.barbie = 50
if args.cars not in range(0, 101):
    args.cars = 50
boy = int((100 - args.barbie + args.cars + dct[args.movie]) / 3)
girl = (100 - boy)
print('boy:', boy)
print('girl:', girl)