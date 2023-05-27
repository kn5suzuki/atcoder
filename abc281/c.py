n, t = list(map(int, input().split(" ")))
a = list(map(int, input().split(" ")))

loop = 0
for i in a:
    loop += i
tmp = t % loop

for i in range(n):
    if tmp - a[i] < 0:
        print(i + 1, tmp)
        break
    else:
        tmp -= a[i]
