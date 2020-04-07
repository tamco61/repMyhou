import argparse
parser = argparse.ArgumentParser()
parser.add_argument('nums', nargs='*')
arg = parser.parse_args()
try:
    if len(arg.nums) > 2:
        print('TOO MUCH PARAMS')
    elif len(arg.nums) == 2:
        print(int(arg.nums[0]) + int(arg.nums[1]))
    elif arg.nums == list():
        print('NO PARAMS')
    else:
        print('TOO FEW PARAMS')
except BaseException as a:
    print(a.__class__.__name__)