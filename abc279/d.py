import math

a, b = list(map(int, input().split(" ")))
g = 1


def f(x):
    return a / math.sqrt(g + x) + b * x


def solve():
    left = 0
    right = 10**16
    while left <= right:
        m = (left + right) // 2
        if m == 0:
            print(f(0))
            return 0
        tmp1 = f(m - 1)
        tmp2 = f(m)
        tmp3 = f(m + 1)
        if tmp1 >= tmp2 and tmp2 <= tmp3:
            print(tmp2)
            return 0
        elif tmp1 < tmp2:
            right = m - 1
        else:
            left = m + 1


solve()
