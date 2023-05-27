s = input()
t = input()

for i in range(len(t)):
    if i == len(s):
        print(i + 1)
        break
    if s[i] != t[i]:
        print(i + 1)
        break
