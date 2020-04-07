def return_number(number):
    number = [i for i in number if i in '1234567890+']
    if number[0] == '+':
        return ''.join(i for i in number)
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
            return False
    if v + n > 2:
        return False
    if v == 0 and n == 0:
        return True
    elif v == 1 and n == 1:
        return True
def check_dash(number):
    if number[0] != '-' and number[-1] != '-':
        n = 0
        for i in number:
            if i in '1234567890+':
                n = 0
            elif i == '-':
                n += 1
                if n == 2:
                    return False
            else:
                return False
        return True
    return False
def check_first_num(number):
    if (len(number) == 11 and number[0] == '8') or (len(number) == 12 and number[0:2] == ['+', '7']):
        return True
    return False
def program(number):
    number_to = [i for i in number if i in '1234567890+']
    if check_first_num(number_to):
        number_to = [i for i in number if i != ' ' and i in '1234567890+-']
        if check_dash(number_to):
            number_to = [i for i in number if i in '1234567890+()']
            if check_brackets(number_to):
                return return_number(number)
    return 'error'
print(program(input()))