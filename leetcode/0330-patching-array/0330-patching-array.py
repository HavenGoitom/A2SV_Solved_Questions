class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        miss = 0
        i = 0
        patches = 0

        while miss < n:
            if i < len(nums) and nums[i] <= miss+1:
                miss += nums[i]
                i += 1
            else:
                miss += (miss + 1)
                patches += 1

        return patches