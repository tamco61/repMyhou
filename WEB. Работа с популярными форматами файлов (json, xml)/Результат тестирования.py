import json
summa = 0
file = open('input.txt').readlines()
rep = json.loads(open('scoring.json').read())
dct = dict()
lst = list()
for i in range(len(file)):
    if 'ok' in file[i]:
        lst.append(i + 1)
for i in range(len(rep['scoring'])):
    ggg = rep['scoring'][i]['required_pretests']
    t = True
    vvs = rep['scoring'][i]['required_tests']
    n = 0
    for r in range(len(vvs)):
        if vvs[r] in lst:
            n += 1
            summa += rep['scoring'][i]['points'] // len(vvs)
    for r in ggg:
        if r not in lst:
            t = False
            break
    if n == len(vvs) and rep['scoring'][i]['points'] != 0 and t:
        summa += n
print(summa)