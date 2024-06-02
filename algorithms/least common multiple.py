"""
algorithm that finds the least common multiple of two numbers. That is the smallest number that can be divided by two
numbers.  ex) for 24 and 16 it is 48. this can come in handy when adding fractions. you coule multiple the denominator
with the numerators but then you will end up with large number which you will then need to devide to simplify. This
method allows for the denominator to remain small and concise.
"""

def lmc_brute_force(a:int, b:int) -> int:
    """
    brute force method that will take too long.
    :param a:
    :param b:
    :return:
    """
    for d in range(1, a*b+1):
        if d % a == 0 and d % b == 0:
            return d


def lmc(a: int, b: int) -> int:
    """
    this functions relies on the fact that lmc(a,b) * gcd(a, b) == a * b or if we transform it,
    lmc(a, b) = (a*b) / gcd(a, b). So we simply use out gcd function to figure this out.
    :param a:
    :param b:
    :return:
    """
    product = a * b
    while a > 0 and b > 0:
        if a >= b:
            a %= b
        else:
            b %= a
    return product // max(a, b)


if __name__ == '__main__':
    print(lmc(24, 16))
    pass