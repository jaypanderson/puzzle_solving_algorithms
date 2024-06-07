"""
Implement the function FastModularExponentiation(b,k,m)FastModularExponentiation(b,k,m) which computes
b2k mod mb2kmodm  using only around 2k2k modular multiplications. You are not allowed to use Python built-in exponentiation functions.
"""


# this is the slower version
def FastModularExponentiation(b, k, m):
    ans = b % m

    for i in range(k):
        ans = (ans * ans) % m
    return ans

def fast_modular_exponentiation(b, e, m):
    assert m > 0 and e >= 0
    if e == 0:
        return 1
    if e == 1:
        return b
    if e % 2 == 0:
        return fast_modular_exponentiation((b * b) % m, e // 2, m)
    else:
        return (fast_modular_exponentiation(b, e - 1, m) * b) % m


if __name__ == '__main__':
    print(fast_modular_exponentiation(314159265358, 2718281828, 123456789))
    print(fast_modular_exponentiation(2, 238, 239))