from yandex_testing_lesson import strip_punctuation_ru
def test_phone():
    test_data = (
        ('ргкуг:!?-, рпгк,', 'ргкуг рпгк'),
        ('!-_.,', ''),
        ('кого-нибудь', 'кого-нибудь'),
        ('огк  цу!-  уц ,уцу  ц', 'огк цу уц уцу ц'),
        ('цуцу,!  -', 'цуцу   -'),
        ('-', '-'),
        ('ыц- ц', ''),
        ('ц-, ц', ''),
        ('ц-,ц', ''),
        ('ц -, ц', ''),
        ('ц -,ц', ''),
        ('ц,-, ц', ''),
        ('ц, - , ц', ''),
        ('ц, -! , ц', ''),
        ('ц -ц', ''),
        ('ц - ц', '')
    )
    for inp, correct in test_data:
        out = strip_punctuation_ru(inp)
        print(out)
    return False
if test_phone():
    print('YES')
else:
    print('NO')