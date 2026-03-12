class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        max_reached = 0
        if len(nums) == 1:
            return True
        left = 1
        curr = 0
        while left < len(nums):
            nums[curr] -= 1
            if nums[curr] < 0:
                return False
            if nums[left] > nums[curr]:
                curr = left
            left += 1
            
        return True



        # Track the maximum reachable index dynamically; if current index exceeds it, the end is unreachable.