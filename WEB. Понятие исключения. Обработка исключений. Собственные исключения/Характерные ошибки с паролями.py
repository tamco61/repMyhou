class PasswordError(Exception):
    pass
class LengthError(PasswordError):
    pass
class LetterError(PasswordError):
    pass
class DigitError(PasswordError):
    pass
class SequenceError(PasswordError):
    pass
class WordError(PasswordError):
    pass
lst_check = ['check_len(pas)', 'check_register(pas)',
             'check_on_number(pas)', 'check_easy(pas)', 'check_word(pas)']
exception_dct = {
    'WordError': 0,
    'DigitError': 0,
    'LengthError': 0,
    'LetterError': 0,
    'SequenceError': 0
}
num = ['1234567890']
win_en = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
win_ru = ['йцукенгшщзхъ', 'фывапролджэ', 'ячсмитьбю']
mac_en = ['qwertzui', 'asdfghjkl', 'yxcvbnm']
def check_word(pas):
    lst_check = [r.rstrip() for r in open('top-9999-words.txt').readlines()]
    for r in lst_check:
        if r in pas:
            raise WordError('WordError')
    return True
def check_easy(pas):
    pas = pas.lower()
    for i in range(len(pas) - 2):
        for r in [win_en, win_ru]:
            for j in r:
                if pas[i] + pas[i + 1] + pas[i + 2] in j:
                    raise SequenceError('SequenceError')
    return True
def check_on_number(pas):
    for i in pas:
        if i in '1234567890':
            return True
    raise DigitError('DigitError')
def check_register(pas):
    if pas != pas.upper() and pas != pas.lower():
        return True
    raise LetterError('LetterError')
def check_len(pas):
    if len(pas) < 9:
        raise LengthError('LengthError')
    return True
def check_password(pas, func):
    try:
        eval(func)
        return 'ok'
    except PasswordError as e:
        return e
def main():
    global lst_check
    lst_passwd = [r.rstrip() for r in open('top 10000 passwd.txt').readlines()]
    for r in lst_passwd:
        for j in lst_check:
            ret = check_password(r, j)
            if ret != 'ok':
                exception_dct[ret.__class__.__name__] += 1
main()
for i in sorted(exception_dct.keys()):
    print(f'{i} - {exception_dct[i]}')