h, w = list(map(int, input().split(" ")))
a = []
for _ in range(h):
    a.append(input())
b = []
for _ in range(h):
    b.append(input())

for i in range(h):
    for j in range(w):
        is_same = True
        for k in range(h):
            for l in range(w):
                if a[k][l] != b[(i+k)%h][(j+l)%w]:
                    is_same = False
                    break
        if is_same:
            print("Yes")
            exit(0)
print("No")