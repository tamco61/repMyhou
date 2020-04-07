import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--sort', action='store_true')
parser.add_argument('dict', nargs='+')
arg = parser.parse_args()
dct = dict()
for i in arg.dict:
    key, value = i.split('=')
    dct[key] = dct.get(key, value)
    dct[key] = value
if arg.sort:
    lst = sorted(dct.keys())
else:
    lst = dct.keys()
for i in lst:
    print(f'Key: {i}\tValue: {dct[i]}')