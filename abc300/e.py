N = int(input())

def dp(n):
    if n >= N:
        return 1 if n==N else 0
    res = 0