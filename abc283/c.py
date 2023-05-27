s = input()
ans = 0
i = 0
while i < len(s):
    if i + 1 < len(s) and s[i : i + 2] == "00":
        i += 2
    else:
        i += 1
    ans += 1
print(ans)
