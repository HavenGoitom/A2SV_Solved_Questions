class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        left = 0
        right = int(math.sqrt(c))

        if c == 0:
            return True

        while left <= right:
            a = left**2 
            b = right**2

            if a+a == c:
                return True

            if a + b  == c:
                return True
            elif (a+b) < c:
                left += 1
            else:
                right -= 1

        return False
            
