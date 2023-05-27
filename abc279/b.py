s = input()
t = input()


def solve():
    for i in range(len(s) - len(t) + 1):
        for j in range(len(t)):
            if s[i + j] != t[j]:
                break
            if j == len(t) - 1:
                print("Yes")
                return 0
    print("No")


solve()
