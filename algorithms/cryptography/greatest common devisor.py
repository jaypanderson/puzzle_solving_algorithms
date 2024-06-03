"""
algorithm that finds the greatest common devisor between two numbers(gcd)
"""
import time
def gcd_brute_force(a:int, b:int) -> int:
    """
    the brute force method which will take too long for very large numbers
    :param a:
    :param b:
    :return:
    """
    if a < 0 or b < 0:
        print("must be positive numbers")
        return
    if a == 0 or b == 0:
        return max(a, b)

    for num in range(min(a, b), 0, -1):
        if a % num == 0 and b % num == 0:
            return num

def gcd_subtract(a:int, b:int) -> int:
    """
    a better method that avoids a large amount of calculations.
    :param a:
    :param b:
    :return:
    """

    while a > 0 and b > 0:
        print(a, b)
        if a >= b:
            a -= b
        else:
            b -= a
    return max(a, b)


def gcd(a:int, b:int) -> int:
    """
    an improvement over the previous one using modulo.
    :param a:
    :param b:
    :return:
    """
    while a > 0 and b > 0:
        print(a, b)
        if a >= b:
            a %= b
        else:
            b %= a
    return max(a, b)

def gcd_recursive(a:int, b:int) -> int:
    return gcd_recursive(b, a%b) if b > 0 else a


def extended_gcd(a, b):
    """
    this is the entended Euclidian algorithm that calculates the greatest common devisor as well as numbers x and y
    called the certificate that are mutipliers that can be used to mutiple the original numbers that will give the gcd.
    ex a = 391, b = 299  certiciate -> x = -3, y = 4
    if we calculate the gcd then we get 23 which is equal to 391(-3) + 299(4) = -1173 + 1196 = 23
    currently there is an essertion error when b is bigger than a this might simply be an assertion error and may not
    actually affect the code. when using this code for an assignment sinply removing the assertions made it correct.
    :param a:
    :param b:
    :return:
    """
    assert a >= b and b >= 0 and a + b > 0

    if b == 0:
        d, x, y = a, 1, 0
    else:
        (d, p, q) = extended_gcd(b, a % b)
        x = q
        y = p - q * (a // b)

    assert a % d == 0 and b % d == 0
    assert d == a * x + b * y
    return (d, x, y)


if __name__ == '__main__':
#
# Examples that can be used
# (69620001, 1044300000)
# (790933790548, 7) this is extremely slow with the first two functions.
# (79093379054, 1849639579327)
# (74849302198574637289038758439302193847583958734903028494857483910394758271849503298765212098754125698, 5469578565231556458595458652545856957542568547932654789652312524569899889653624759658745895854785)
# 391, 299

    # start = time.time()
    # for i in range(1):
    #     print(gcd(74849302198574637289038758439302193847583958734903028494857483910394758271849503298765212098754125698, 5469578565231556458595458652545856957542568547932654789652312524569899889653624759658745895854785))
    # print(time.time() - start)

    # print(gcd_recursive(48, 64))

    print(extended_gcd(1980, 1848))

