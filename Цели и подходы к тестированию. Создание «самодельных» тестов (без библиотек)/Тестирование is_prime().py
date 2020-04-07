from yandex_testing_lesson import is_prime
def test_prime():
    test_data = (
        (9293, True),
        (66, False),
        (29, True),
        (2, True),
        (10, False),
        (3, True),
        (9, False),
        (15, False),
        (31, True)
    )
    for inp, correct in test_data:
        out = is_prime(inp)
        if out != correct:
            return False
    return True
if test_prime():
    print('YES')
else:
    print('NO')