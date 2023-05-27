n = int(input())
s = input()

def solve(s):
    count = 0
    for letter in s:
        if letter == "|":
            count += 1
        elif letter == "*":
            if count == 1:
                print("in")
            else:
                print("out")

solve(s)