import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--count', action='store_true')
parser.add_argument('--num', action='store_true')
parser.add_argument('--sort', action='store_true')
parser.add_argument('file')
arg = parser.parse_args()
try:
    file = open(arg.file).readlines()
    file = [i.rstrip() for i in file]
    if arg.sort:
        vvs = list(file)[1:]
        vvs.sort()
        file = [file[0]]
        for i in vvs:
            file.append(i)
    if arg.num:
        for i in range(len(file)):
            file[i] = f'{i} {file[i]}'
    if arg.count:
        file.append(f'rows count: {len(file)}')
    for i in file:
        print(i)
except BaseException:
    print('ERROR')