from yandex_testing_lesson import strip_punctuation_ru
def test_phone():
    test_data = (
        ('ргкуг:!?-, рпгк,', 'ргкуг рпгк'),
        ('кого-нибудь', 'кого-нибудь'),
        ('огк  цу!-  уц ,уцу  ц', 'огк цу уц уцу ц'),
        ('цуцу,!-', 'цуцу -'),
        ('-', '-')
    )
    for inp, correct in test_data:
        out = strip_punctuation_ru(inp)
        if out != correct:
            return False
    return True
if test_phone():
    print('YES')
else:
    print('NO')
