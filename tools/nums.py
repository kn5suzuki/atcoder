def prime_all(n):
    is_prime = [True]*(n+1)
    is_prime[0] = is_prime[1] = False
    i = 2
    while i*i <= n:
        if is_prime[i]:
            j = 2
            while i*j <= n:
                is_prime[i*j] = False
                j += 1
        i += 1
    return [i for i in range(2, n+1) if is_prime[i]]