k = int(input())


def calc(n, c):
    i = 1
    ans = 1
    while i < c:
        tmp = n * ans
        while tmp % n == 0:
            tmp /= n
            i += 1
        ans += 1
    return ans


ans = 0
i = 2
while i * i <= k:
    count = 0
    tmp = k
    while tmp % i == 0:
        count += 1
        tmp //= i
    min_ans = i * calc(i, count)
    if min_ans > ans:
        ans = min_ans
    if ans < k // (i * count) and prime(k // (i * count)):
        ans = k // (i * count)
    i += 1

if ans == 0:
    ans = k
print(ans)
