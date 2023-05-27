n, m = list(map(int, input().split(" ")))


def solve():
    if m == 0:
        for i in range(n):
            print(i + 1, end=" ")
        return 0
    a = list(map(int, input().split(" ")))

    tmp = 1
    i = 0
    while i < len(a):
        while tmp < a[i]:
            print(tmp, end=" ")
            tmp += 1
        count = 1
        i += 1
        while i < len(a) and a[i] - 1 == a[i - 1]:
            i += 1
            count += 1
        for j in range(count + 1):
            print(tmp + count - j, end=" ")
        tmp += count + 1
    while tmp <= n:
        print(tmp, end=" ")
        tmp += 1
    return 0


solve()
