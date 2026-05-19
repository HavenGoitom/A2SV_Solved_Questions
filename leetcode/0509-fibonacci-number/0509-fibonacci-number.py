class Solution:
    def fib(self, n: int) -> int:
        memo = {}

        def helper(n):
            if n == 1 or n == 0:
                return n
            if n not in memo:
                memo[n] = self.fib(n-1) + self.fib(n-2)
            return memo[n]
            
        return helper(n)