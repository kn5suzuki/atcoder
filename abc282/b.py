n, m = list(map(int, input().split(" ")))

s = []
for i in range(n):
    s.append(input())

ans = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        for k in range(m):
            if s[i][k] == "x" and s[j][k] == "x":
                break
            if k == m - 1:
                ans += 1
print(ans)
