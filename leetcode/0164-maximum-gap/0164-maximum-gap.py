class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) < 2:
            return 0
            
        res = float('-inf')
        for i in range(len(nums)-1):
            res = max(res, nums[i+1] - nums[i])
        
        return res