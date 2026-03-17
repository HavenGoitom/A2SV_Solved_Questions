class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # odd = {2 3 5 7} 4
        # even = {0 2 4 6 8} 5
        # if n == 1:
        #     return 5
        MOD = 10**9 + 7
        
        even = ceil(n/2)
        odd = floor(n/2)
        # print(odd,even)
        
        def helper(n,x):
            if n == 0:
                return 1
            
            res = helper(n//2,x)
            if n % 2 == 0:
                return res * res % MOD
            else:
                return x * res * res % MOD
        
        odd_ans = helper(odd,4)
        even_ans = helper(even,5)
        # print(odd_ans, even_ans)
        return (odd_ans * even_ans) % MOD