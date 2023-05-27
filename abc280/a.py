h, w = list(map(int, input().split(" ")))

count = 0
for i in range(h):
    s = input()
    count += s.count("#")
print(count)
