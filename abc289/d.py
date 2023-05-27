n = int(input())
a = list(map(int, input().split(" ")))
m = int(input())
b = list(map(int, input().split(" ")))
x = int(input())

s = [0 for _ in range(x + 1)]
for i in range(m):
    s[b[i]] = -1
s[0] = 1
for i in range(x):
    if s[i] == 1:
        for j in range(n):
            if i + a[j] <= x and s[i + a[j]] != -1:
                s[i + a[j]] = 1
if s[x] == 1:
    print("Yes")
else:
    print("No")
