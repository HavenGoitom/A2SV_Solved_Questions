class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left = 1 #min candie
        right = max(candies) #max candie
        ans = 0

        def canDivide(ans):
            count = 0
            for candie in candies:
                count += candie // ans
            return count >= k

        while left <= right:
            candie = (left + right) // 2
            if canDivide(candie):
                ans = max(ans, candie)
                left = candie + 1
            else:
                right = candie - 1

        return ans

