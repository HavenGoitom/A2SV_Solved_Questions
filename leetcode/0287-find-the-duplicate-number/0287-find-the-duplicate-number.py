class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ans = 0
        nums_set = set()

        for num in nums:
            if num in nums_set:
                ans = num
                break
            nums_set.add(num)

        # print(nums_set)
        return ans