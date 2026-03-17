class Solution:
    def myPow(self, x: float, n: int) -> float:
        # return x**n

        def helper(x,n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            res = helper(x, n//2)
            if n % 2 == 0:
                return res * res # 2^10 = 2^5 * 2^5
            else:
                return x * res * res #2^5 = 2 * 2^4 *2^4

        if n >= 0:
            return helper(x,abs(n))
        else:
            return 1/helper(x,abs(n))
        