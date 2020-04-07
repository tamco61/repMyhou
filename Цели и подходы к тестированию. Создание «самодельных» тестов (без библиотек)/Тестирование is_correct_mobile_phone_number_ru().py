from yandex_testing_lesson import is_correct_mobile_phone_number_ru
def test_phone():
    test_data = (
        ('+7(900)1234567', True),
        ('8(900)1234567', True),
        ('+79001234567', True),
        ('89001234567', True),
        ('89000', False),
        ('+79001234', False),
        ('+7(900)12345', False),
        ('8(900)12347', False),
        ('7(900)1234567', False),
        ('+8(900)1234567', False),
        ('+7 999 123-45-67', True),
        ('8 999 123-45-67', True),
        ('+7 (999) 123-45-67', True),
        ('8 (999) 123-45-67', True),
        ('+7 (999 123-45-67', False),
        ('8 (999 123-45-67', False)
    )
    for inp, correct in test_data:
        out = is_correct_mobile_phone_number_ru(inp)
        if out != correct:
            return False
    return True
if test_phone():
    print('YES')
else:
    print('NO')