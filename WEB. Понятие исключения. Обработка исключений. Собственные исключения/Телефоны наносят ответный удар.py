oper_list = [i for i in range(910, 940)] + [i for i in range(902, 907)] +\
            [i for i in range(960, 970)] + [i for i in range(980, 990)]
class Error(Exception):
    pass
class InvalidFormat(Error):
    pass
class InvalidLen(Error):
    pass
class InvalidOperator(Error):
    pass
def check_operators(number):
    global oper_list
    if int(''.join(i for i in number[1:4])) in oper_list:
        return True
    raise InvalidOperator('не определяется оператор сотовой связи')
def return_number(number):
    number = [i for i in number if i in '1234567890']
    if number[0] == '7':
        return '+' + ''.join(i for i in number)
    else:
        return '+7' + ''.join(i for i in number[1:])
def check_brackets(number):
    n = 0
    v = 0
    for i in number:
        if i == '(':
            n += 1
        elif i == ')':
            v += 1
        if v + n > 2:
            raise InvalidFormat('неверный формат')
    if v == 0 and n == 0:
        return True
    elif v == 1 and n == 1:
        return True
    raise InvalidFormat('неверный формат')
def check_dash(number):
    if number[0] != '-' and number[-1] != '-':
        n = 0
        for i in number:
            if i in '1234567890+':
                n = 0
            elif i == '-':
                n += 1
                if n == 2:
                    raise InvalidFormat('неверный формат')
            else:
                raise InvalidFormat('неверный формат')
        return True
    raise InvalidFormat('неверный формат')
def check_first_num(number):
    if number[0:2] == ['+', '7'] or number[0] == '8':
        if (len(number) == 11 and number[0] == '8') or (len(number) == 12 and number[0] == '+'):
            return True
        else:
            raise InvalidLen('неверное количество цифр')
    raise InvalidFormat('неверный формат')
def process(number):
    try:
        if len(number) == len([i for i in number if i in '1234567890+ -()\t']):
            number_to = [i for i in number if i != ' ' and i in '1234567890-']
            if check_dash(number_to):
                number_to = [i for i in number if i in '1234567890()']
                if check_brackets(number_to):
                    number_to = [i for i in number if i in '1234567890+']
                    if check_first_num(number_to):
                        number_to = [i for i in number if i in '1234567890']
                        if check_operators(number_to):
                            return return_number(number)
        raise InvalidFormat('неверный формат')
    except Error as e:
        return e
print(process(input()))