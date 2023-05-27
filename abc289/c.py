n, m = list(map(int, input().split(" ")))
s = []
for _ in range(m):
    c = int(input())
    a = set(map(int, input().split(" ")))
    s.append(a)


def select(i, tmp, ans):
    if i == m:
        if len(tmp) == n:
            return ans + 1
        else:
            return ans
    ans = select(i + 1, tmp, ans)
    ans = select(i + 1, tmp.union(s[i]), ans)
    return ans


print(select(0, set(), 0))
