n, k, d = list(map(int, input().split(" ")))
a = list(map(int, input().split(" ")))


dp = [[[-1 for _ in range(d)] for _ in range(n)] for _ in range(k + 1)]
for i in range(n):
    dp[0][i][0] = 0

tmp = 0
for i in range(k):
    tmp += a[i]
    dp[i + 1][i][tmp % d] = tmp

for i in range(1, k + 1):
    for j in range(i, n):
        for l in range(d):
            if dp[i - 1][j - 1][(l - a[j] % d) % d] != -1:
                dp[i][j][l] = max(
                    dp[i][j - 1][l], dp[i - 1][j - 1][(l - a[j] % d) % d] + a[j]
                )
            else:
                dp[i][j][l] = dp[i][j - 1][l]

ans = dp[k][n - 1][0]
if ans == -1:
    print(-1)
else:
    print(ans)
