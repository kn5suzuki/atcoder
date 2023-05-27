n, k = list(map(int, input().split(" ")))
a = list(map(int, input().split(" ")))
q = int(input())

a_ = []
for i in range(n):
    tmp = a[i]
    a_.append(tmp)
    for j in range(k):
        if i + j < n:
            a[i + j] -= tmp

for i in range(q):
    l, r = list(map(int, input().split(" ")))
