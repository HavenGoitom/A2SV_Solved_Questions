class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        j = 1
        for i in range(len(nums)):
            if nums[i] == j:
                j += 1
        return j