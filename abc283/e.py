h, w = list(map(int, input().split(" ")))
a = []
for i in range(h):
    tmp = list(map(int, input().split(" ")))
    a.append(tmp)

f = lambda x: 1 - x

reverse_or_not = [0 for i in range(h)]


def solve():
    ans = 0
    mini_ans = 0
    total = 0
    for i in range(h):
        total += 1
        if i == h - 1:
            for j in range(w):
                if not (j > 0 and a[i][j - 1] == a[i][j]) or (
                    j < w - 1 and a[i][j] == a[i][j + 1]
                ):
                    if reverse_or_not[i] == 0 and a[i][j] == a[i - 1][j]:
                        reverse_or_not[i] = -1
                    elif reverse_or_not[i] == 0 and a[i][j] != a[i - 1][j]:
                        reverse_or_not[i] = 1
                    elif reverse_or_not[i] == -1 and a[i][j] != a[i - 1][j]:
                        return -1
                    elif reverse_or_not[i] == 1 and a[i][j] == a[i - 1][j]:
                        return -1
            if reverse_or_not[i] != 0:
                mini_ans += 1
            ans += min(mini_ans, total - mini_ans)

        else:
            for j in range(w):
                if not (
                    (i > 0 and a[i][j] == a[i - 1][j])
                    or (j > 0 and a[i][j - 1] == a[i][j])
                    or (j < w - 1 and a[i][j] == a[i][j + 1])
                ):
                    if i + 1 < h and a[i][j] == a[i + 1][j]:
                        if reverse_or_not[i + 1] == 1:
                            return -1
                        reverse_or_not[i + 1] = -1
                    elif i + 1 < h and a[i][j] != a[i + 1][j]:
                        if reverse_or_not[i + 1] == -1:
                            return -1
                        reverse_or_not[i + 1] = 1

            if reverse_or_not[i + 1] == 0:
                ans += min(mini_ans, total - mini_ans)
                mini_ans = 0
                total = 0
            elif reverse_or_not[i + 1] == 1 and i + 1 != h - 1:
                a[i + 1] = list(map(f, a[i + 1]))
                mini_ans += 1
    return ans


print(solve())
