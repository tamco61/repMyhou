from zipfile import ZipFile
word = ''
n = 0
zip = ZipFile('input.zip')
registry = zip.namelist()
def func(word, n, mask=None):
    if mask is None:
        mask = []
    for i in registry:
        if '/' in i:
            w = i.split('/')
        else:
            w = ''
        if i[-1] == '/':
            if mask == list() and len(w) == 2:
                word += ' ' * n + w[-2] + '\n'
                lst = list(mask)
                lst.append(w[-2])
                word += func('', n + 2, lst)
            elif mask == w[:-2] and len(mask) + 2 == len(w):
                word += ' ' * n + w[-2] + '\n'
                lst = list(mask)
                lst.append(w[-2])
                word += func('', n + 2, lst)
        else:
            if mask == list() and w == '':
                word += ' ' * n + i + '\n'
            elif mask == w[:-1]:
                word += ' ' * n + w[-1] + '\n'
    return word
print(func(word, n))