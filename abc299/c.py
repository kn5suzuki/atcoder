n = int(input())
s = input()

def solve(s):
    ans = 0
    counting = False
    valid = False
    tmp = 0
    for letter in s:
        if letter == "-":
            valid = True
        if letter == "o" and not counting:
            counting = True
            tmp = 1
        elif letter == "o" and counting:
            tmp += 1
        elif letter == "-" and counting:
            counting = False
            ans = tmp if tmp > ans else ans
    if counting and valid and tmp > ans:
        ans = tmp
    return ans if ans > 0 and valid else -1

print(solve(s))