h, w = list(map(int, input().split(" ")))
c = []
for _ in range(h):
    c.append(input())

n = min(h,w)
ans = [0 for i in range(n)]
for i in range(h):
    for j in range(w):
        if c[i][j] == "#":
            k = 0
            while k < n-1:
                try:
                    if c[i+(k+1)][j+(k+1)] == "#" and c[i+(k+1)][j-(k+1)] == "#" and c[i-(k+1)][j+(k+1)] == "#" and c[i-(k+1)][j-(k+1)] == "#":
                        k += 1
                    else:
                        break
                except:
                    break
            if k > 0:
                ans[k-1] += 1

for v in ans:
    print(v, end=" ")
