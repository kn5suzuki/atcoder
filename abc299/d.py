n = int(input())

left = 0
right = n-1
for i in range(20):
    pivot = (left + right) // 2
    print(f"? {pivot+1}")
    ans = int(input())
    if ans == 0:
        left = pivot
    else:
        right = pivot
    if left+1 == right:
        print(f"! {left+1}")