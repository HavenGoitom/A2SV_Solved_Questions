class Solution:
    def lastRemaining(self, n: int) -> int:
        
        def helper(n):
            if n == 1:
                return 1
            return 2 * (n//2 + 1 - helper(n//2))
            
        return helper(n)