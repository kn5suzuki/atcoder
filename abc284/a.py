n = int(input())
strings = []
for i in range(n):
    strings.append(input())
for i in range(n):
    print(strings[n - i - 1])
