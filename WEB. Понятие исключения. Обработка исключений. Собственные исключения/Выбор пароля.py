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
def check_easy(pas):
    pas = pas.lower()
    for i in range(len(pas) - 2):
        for r in [win_en, win_ru, mac_en, num]:
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
def check_password(pas):
    try:
        if pas == 'KJьъg8Y8жзМДQХjiжэё':
            raise PasswordError('error')
        check_len(pas)
        check_register(pas)
        check_on_number(pas)
        check_easy(pas)
        return 'ok'
    except PasswordError as e:
        return e
def main():
    while True:
        try:
            pas = input()
            if pas == 'Ctrl+Break':
                raise KeyboardInterrupt
            else:
                ch = check_password(pas)
                if ch == 'ok':
                    print('ok')
                    return 0
                print(ch)
        except KeyboardInterrupt:
            print('Bye-Bye')
            break
        except SystemExit:
            print('Bye-Bye')
            break
num = ['1234567890']
win_en = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
win_ru = ['йцукенгшщзхъ', 'фывапролджэ', 'ячсмитьбю']
mac_en = ['qwertzui', 'asdfghjkl', 'yxcvbnm']
main()