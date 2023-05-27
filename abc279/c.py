h, w = list(map(int, input().split(" ")))

s = []
t = []
for _ in range(h):
    s.append(input())
for _ in range(h):
    t.append(input())

s_t = []
for i in range(w):
    tmp = ""
    for j in range(h):
        tmp += s[j][i]
    s_t.append(tmp)

t_t = []
for i in range(w):
    tmp = ""
    for j in range(h):
        tmp += t[j][i]
    t_t.append(tmp)

if sorted(s_t) == sorted(t_t):
    print("Yes")
else:
    print("No")
