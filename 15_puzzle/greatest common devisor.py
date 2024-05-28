def gcd(a:int, b:int) -> int:
    if a < 0 or b < 0:
        print("must be positive numbers")
        return
    if a == 0 or b == 0:
        return max(a, b)

    for num in range(min(a, b), 0, -1):
        if a % num == 0 and b % num == 0:
            return num


if __name__ == '__main__':
    print(gcd(6962, 10443))
