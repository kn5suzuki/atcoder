from math import isqrt

n = int(input())

is_prime = [True]*(isqrt(n+1))
is_prime[0] = is_prime[1] = False
i = 2
while i*i < len(is_prime):
    if is_prime[i]:
        j = 2
        while i*j < len(is_prime):
            is_prime[i*j] = False
            j += 1
    i += 1
primes = [i for i in range(2, len(is_prime)) if is_prime[i]]

prefix_sum = is_prime
for i in range(len(prefix_sum)-1):
  prefix_sum[i+1] += prefix_sum[i]

ans = 0
for i in range(len(primes)):
  a = primes[i]
  if a * a * a * a * a >= n:
    break
  for j in range(i + 1, len(primes)):
    b = primes[j]
    if a * a * b * b * b >= n:
      break
    ans += prefix_sum[isqrt(n // (a * a * b))] - prefix_sum[b]
print(ans)