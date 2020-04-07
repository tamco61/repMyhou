import os
s_first = os.getcwd()
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
def main(s):
    os.chdir(s)
    lst = os.listdir()
    lst_get = list()
    for i in lst:
        os.chdir(s)
        if os.path.isfile(i):
            lst_get.append([i, os.path.getsize(i)])
            continue
        lst_get.append([i, get_size(s + '/' + i)])
    lst_get.sort(key=lambda x: x[1], reverse=True)
    if len(lst_get) > 10:
        lst_get = lst_get[:10]
    m_len = 0
    for i in lst_get:
        if len(i[0]) > m_len:
            m_len = len(i[0])
    for i in lst_get:
        print(f'{i[0]}{(m_len - len(i[0])) * " "}     - {human_read_format(i[1])}')
def get_size(s):
    os.chdir(s)
    lst = os.listdir()
    n = 0
    for i in lst:
        os.chdir(s)
        if os.path.isfile(i):
            n += os.path.getsize(i)
            continue
        n += get_size(s + '/' + i + '/')
    return n
main(s_first)