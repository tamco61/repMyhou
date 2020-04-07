from zipfile import ZipFile
import json
n = 0
with ZipFile('input.zip') as myzip:
    lst = myzip.namelist()[1:]
    for i in lst:
        dct = json.loads(myzip.open(i, 'r').read(), encoding='UTF-8')
        if dct['city'] == 'Москва':
            n += 1
print(n)