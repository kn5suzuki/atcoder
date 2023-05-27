import math


def solve(n):
    for i in range(2, 10**7):
        if n % i == 0:
            n = n // i
            if n % i == 0:
                return i, n // i
            else:
                return int(math.sqrt(n)), i


t = int(input())
for i in range(t):
    n = int(input())
    p, q = solve(n)
    print(p, q)
