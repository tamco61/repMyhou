from zipfile import ZipFile, ZipInfo
import os
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
                i = i + ' ' + human_read_format(zip.getinfo(i).file_size)
                word += ' ' * n + i + '\n'
            elif mask == w[:-1]:
                i = w[-1] + ' ' + human_read_format(zip.getinfo(i).file_size)
                word += ' ' * n + i + '\n'
    return word
def human_read_format(size):
    n = 0
    while True:
        if size // 1024 > 0:
            size = round(size / 1024)
            n += 1
        else:
            break
    form = ''
    if n == 0:
        form = 'Б'
    elif n == 1:
        form = 'КБ'
    elif n == 2:
        form = 'МБ'
    elif n == 3:
        form = 'ГБ'
    return str(size) + form
print(func(word, n))