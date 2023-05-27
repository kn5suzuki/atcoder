n, k = list(map(int, input().split(" ")))
l = []
for i in range(k):
    l.append(input())
l.sort()
for i in range(k):
    print(l[i])
