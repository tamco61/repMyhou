def strip_punctuation_ru(data):
    out_data = ''
    t = True
    v = False
    a = 'йцукенгшщзхъфывапролджэячсмитьб1234567890ю'
    b = 'йцукенгшщзхъфывапролджэячсмитьбю'.upper()
    for i in range(len(data)):
        if data[i] in a + b:
            if t:
                if v:
                    out_data += '-'
                    v = False
                out_data += data[i]
            else:
                if v:
                    out_data += ' ' + '-' + data[i]
                    v = False
                else:
                    out_data += ' ' + data[i]
                t = True
        elif data[i] == '-':
            if t:
                out_data += data[i]
            else:
                v = True
        else:
            t = False
            v = False
        if i + 1 == len(data) and data[i] == '-':
            if out_data[-1] != '-':
                out_data += ' -'
    return out_data