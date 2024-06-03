def gcd(a, b):
    assert a >= 0 and b >= 0 and a + b > 0

    while a > 0 and b > 0:
        if a >= b:
            a = a % b
        else:
            b = b % a
    return max(a, b)


def extended_gcd(a, b):
    if b == 0:
        d, x, y = a, 1, 0
    else:
        (d, p, q) = extended_gcd(b, a % b)
        x = q
        y = p - q * (a // b)

    return (d, x, y)


def divide(a, b, n):
    assert n > 1 and a > 0 and gcd(a, n) == 1
    d, x, y = extended_gcd(a, n)

    return (b * (x % n)) % n

    # return the number x s.t. x = b / a (mod n) and 0 <= x <= n-1.

if __name__ == '__main__':
    # This would calculate x = 7/2 mod 9 or rather 2x mod 9 = 7 and we are solving for x.

    print(divide(7, 2, 9))
