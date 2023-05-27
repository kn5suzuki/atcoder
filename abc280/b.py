n = int(input())
s = list(map(int, input().split(" ")))

print(s[0], end=" ")
for i in range(1, n):
    print(s[i] - s[i - 1], end=" ")
