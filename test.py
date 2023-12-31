import time


def primes_trial_division(n):
    primes = []
    i = 2
    while len(primes) < n:
        for p in primes:
            if i % p == 0:
                break
        else:
            primes.append(i)
        i += 1
    return primes

def primes_sieve(n):
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    for x in range(2, int(n**0.5) + 1):
        if sieve[x]:
            sieve[2*x::x] = [False] * len(sieve[2*x::x])
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


n = 20000

start = time.time()
primes_trial_division(n)
end = time.time()
print("Time taken by trial division: ", end - start)

start = time.time()
primes_sieve(n)
end = time.time()
print("Time taken by sieve of eratosthenes: ", end - start)
