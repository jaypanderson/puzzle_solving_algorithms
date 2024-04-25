"""
simulates the galton board and you can choose the depth of the galton board. This does not make you of random number
generators so the answer will be exact every single time. it specically calculates the amount between the 40 percent and
60 percent area
"""

from itertools import product

ans = [1]
n = 50

for i in range(2, n+1):
    temp = [None] * i
    for j, num in enumerate(temp):
        if j == 0:
            temp[j] = ans[j] / 2
        elif j != i-1:
            temp[j] = (ans[j] + ans[j - 1]) / 2
        else:
            temp[j] = ans[j - 1] / 2

    ans = temp

print(ans)
print(len(ans))
print(sum(ans[int(n * 0.4):int(n * 0.6)]))
