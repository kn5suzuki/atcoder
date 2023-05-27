s = input()

is_in = [0 for _ in range(26)]


def solve():
    n = 1
    for i in range(len(s)):
        if s[i] == "(":
            n += 1
        elif s[i] == ")":
            for j in range(26):
                if is_in[j] == n:
                    is_in[j] = 0
            n -= 1
        else:
            if is_in[ord(s[i]) - ord("a")] != 0:
                return False
            else:
                is_in[ord(s[i]) - ord("a")] = n
    return True


if solve():
    print("Yes")
else:
    print("No")
