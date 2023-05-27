s = input()

count = 0
for l in s:
    if l == "v":
        count += 1
    elif l == "w":
        count += 2
print(count)
