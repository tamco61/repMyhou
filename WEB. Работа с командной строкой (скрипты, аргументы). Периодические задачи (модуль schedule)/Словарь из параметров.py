import sys
dct = dict()
lst = sys.argv
for i in lst:
    if '=' in i:
        k, v = i.split('=')
        dct[k] = dct.get(k, v)
if len(lst) > 1:
    if '--sort' in lst:
        for i in sorted(dct.keys()):
            print(f'Key: {i} Value: {dct[i]}')
    else:
        for i in dct.keys():
            print(f'Key: {i} Value: {dct[i]}')