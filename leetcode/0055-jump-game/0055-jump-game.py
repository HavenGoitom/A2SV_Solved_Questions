class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        right = 1
        curr = 0
        while right < len(nums):
            nums[curr] -= 1
            if nums[curr] < 0:
                return False
            if nums[right] > nums[curr]:
                curr = right
            right += 1

        return True



        # Track the maximum reachable index dynamically; if current index exceeds it, the end is unreachable.