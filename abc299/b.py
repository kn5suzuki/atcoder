n, t = list(map(int, input().split(" ")))
c = list(map(int, input().split(" ")))
r = list(map(int, input().split(" ")))
t_ = c[0]

winner = 0
winner_ = 1
max_num = 0
max_num_ = 0
for i, color in enumerate(c):
    if color == t:
        if max_num < r[i]:
            max_num = r[i]
            winner = i+1
    elif color == t_:
        if max_num_ < r[i]:
            max_num_ = r[i]
            winner_ = i+1
if winner == 0:
    print(winner_)
else:
    print(winner)

