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

if __name__ == '__main__':
#
# Examples that can be used
# (69620001, 1044300000)
# (790933790548, 7) this is extremely slow with the first two functions.
# (79093379054, 1849639579327)
# (74849302198574637289038758439302193847583958734903028494857483910394758271849503298765212098754125698, 5469578565231556458595458652545856957542568547932654789652312524569899889653624759658745895854785)

    # start = time.time()
    # for i in range(1):
    #     print(gcd(74849302198574637289038758439302193847583958734903028494857483910394758271849503298765212098754125698, 5469578565231556458595458652545856957542568547932654789652312524569899889653624759658745895854785))
    # print(time.time() - start)

    print(gcd_recursive(48, 64))

