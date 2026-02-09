from collections import Counter
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_counter = Counter(nums)

        for num in nums_counter.keys():
            if nums_counter[num] > 1:
                return True  
        return False