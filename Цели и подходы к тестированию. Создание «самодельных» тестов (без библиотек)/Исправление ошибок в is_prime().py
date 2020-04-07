def is_prime(n):
    if n > 1:
        for divisor in range(2, int((n ** 0.5).real) + 1):
            if n % divisor == 0:
                return False
    else:
        return False
    return True
if is_prime(int(input())):
    print('YES')
else:
    print('NO')