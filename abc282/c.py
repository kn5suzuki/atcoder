n = int(input())
s = input()

ans = ""
is_in = False
for i in range(n):
    if s[i] == '"':
        is_in = not is_in
    if s[i] == "," and not is_in:
        ans += "."
    else:
        ans += s[i]
print(ans)
