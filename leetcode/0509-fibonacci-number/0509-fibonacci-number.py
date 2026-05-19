class Solution:
    def fib(self, n: int) -> int:
        hashmap = {}

        if n == 1 or n == 0:
            return n
        if n not in hashmap:
            hashmap[n] = self.fib(n-1) + self.fib(n-2)
        return hashmap[n]