class Solution:
    """https://leetcode.com/problems/count-primes/solution/ """
    def countPrimes(self, n: int) -> int:
        if n == 0:
            return 0
        prime = [True] * n  # init flag memory
        i = 2
        while i*i < n:
            if prime [i] == True:
                # Update all multiples of i to False
                for j in range (i*i, n, i):
                    """
                    The question now is why should we start at i*i. Why not start at 2*i to keep things simple? The reason is that all of the previous multiples 
                    would already have been covered by previous primes. In number theory, the fundamental theorem of arithmetic, also called the unique factorization theorem 
                    or the unique prime factorization theorem, states that every integer greater than 1 either is a prime number itself or can be represented as the product
                    of prime numbers.
                    So the prime numbers smaller than i would have already covered the multiples smaller than i*i. Let's look at the prime number 7 to see how all the multiples
                    up to 7*7 are already covered by primes smaller than '7'.

                    Let's assume that n is 50 (a value greater than 7*7) to demonstrate this claim. 

                    7 * 2 = 14 = 2 * 7
                    7 * 3 = 21 = 3 * 7
                    7 * 4 = 28 = 2 * 2 * 7 = 2 * 14
                    7 * 5 = 35 = 5 * 7
                    7 * 6 = 42 = 2 * 3 * 7 = 2 * 21
                    """
                    prime [j] = False
            i += 1
        total = 0
        for i in range (2, n):
            if prime [i] == True:
                total += 1
        return total
