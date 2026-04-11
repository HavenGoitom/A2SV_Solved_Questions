class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # [-2, -1, -4, 0, -1, 1, 2, -3, 1]
        res = nums[0]
        total = 0

        res = nums[0]
        total = 0

        for num in nums:
            total = max(num, total + num)
            res = max(res, total)
        
        return res