class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # nums.sort() nlogn
        n = len(nums)
        for i in range(n):
            while 0 < nums[i] < n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        j = 1
        for i in range(n):
            if nums[i] == j:
                j += 1
        return j

       