n, a, b = list(map(int, input().split(" ")))
c = list(map(int, input().split(" ")))
for i, v in enumerate(c):
    if v == a+b:
        print(i+1)
        exit(0)