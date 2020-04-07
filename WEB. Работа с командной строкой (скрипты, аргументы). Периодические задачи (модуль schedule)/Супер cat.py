import sys
class Error(Exception):
    pass
def get_filename(lst):
    for i in lst:
        if '.' in i:
            return i
    raise Error
def check_num(lst):
    if '--num' in lst:
        return True
    return False
def check_sort(lst):
    if '--sort' in lst:
        return True
    return False
def check_count(lst):
    if '--count' in lst:
        return True
    return False
lst = sys.argv[1:]
try:
    try:
        filename = get_filename(lst)
        ls = open(filename).readlines()
        if check_sort(lst):
            vvl = list()
            vvl.append(ls[0])
            for i in sorted(ls[1:]):
                vvl.append(i)
            ls = vvl
        if check_num(lst):
            for i in range(len(ls)):
                print(f'{i} {ls[i]}')
        else:
            for i in range(len(ls)):
                print(f'{ls[i]}')
        if check_count(lst):
            print(f'rows count: {len(ls)}')
    except FileNotFoundError:
        print('ERROR')
except Error:
    print('ERROR')