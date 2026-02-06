from collections import Counter
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_dict = Counter(nums)

        for key in nums_dict:
            if nums_dict[key] < 2:
                return key