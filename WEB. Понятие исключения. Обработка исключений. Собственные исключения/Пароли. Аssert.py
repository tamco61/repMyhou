win_en = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
win_ru = ['йцукенгшщзхъ', 'фывапролджэ', 'ячсмитьбю']
mac_en = ['qwertzui', 'asdfghjkl', 'yxcvbnm']
def check_easy(pas):
    pas = pas.lower()
    for i in range(len(pas) - 2):
        for r in [win_en, win_ru, mac_en]:
            for j in r:
                if pas[i] + pas[i + 1] + pas[i + 2] in j:
                    return False
    return True
def check_on_number(pas):
    for i in pas:
        if i in '1234567890':
            return True
    else:
        return False
def check_register(pas):
    if pas != pas.upper() and pas != pas.lower():
        return True
    return False
def check_len(pas):
    if len(pas) <= 8:
        return False
    return True
def program(pas):
    try:
        assert pas != 'KJьъg8Y8жзМДQХjiжэё'
        assert check_len(pas) is True
        assert check_register(pas) is True
        assert check_on_number(pas) is True
        assert check_easy(pas) is True
        return 'ok'
    except AssertionError:
        return 'error'
print(program(input()))