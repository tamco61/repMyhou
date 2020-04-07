from yandex_testing_lesson import is_palindrome
def test_palindrome():
    test_data = (
        ('12321', True),
        ('123', False),
        ('a', True),
        ('aba', True),
        ('tyewq', False),
        ('qwertyytrewq', True),
        ('plmsmlp', True)
    )
    for inp, correct in test_data:
        out = is_palindrome(inp)
        if out != correct:
            return False
    return True
if test_palindrome():
    print('YES')
else:
    print('NO')