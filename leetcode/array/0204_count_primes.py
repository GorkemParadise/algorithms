"""
Problem: 204. Count Primes
Link: https://leetcode.com/problems/count-primes/
Difficulty: Medium
"""


def countPrimes(n):
    if n <= 2:
        return 0
    isPrime = [True] * n
    isPrime[0] = isPrime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if isPrime[i]:
            for j in range(i * i, n, i):
                isPrime[j] = False
    return sum(isPrime)

## TIME: O(n log log n) - Sieve of Eratosthenes algorithm



## TIME: O(n * sqrt(n)) - Naive approach to check each number for primality
    def isPrime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        while n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    

    def countPrimes(n: int) -> int:
        ans = []
        if n < 2:
            return 0
        for k in range(2, n):
            if isPrime(k) == True:
                ans.append(k)
        return ans

