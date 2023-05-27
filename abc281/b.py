s = input()

try:
    s0 = s[0]
    sn = int(s[1:7])
    s7 = s[7]
    if (
        "A" <= s0
        and s0 <= "Z"
        and 100000 <= sn
        and sn <= 999999
        and "A" <= s7
        and s7 <= "Z"
    ):
        print("Yes")
    else:
        print("No")
except:
    print("No")
