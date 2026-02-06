from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_counter = Counter(nums)
        n = len(nums)
        ans = []

        for key in nums_counter:
            if nums_counter[key] > n/3:
                ans.append(key)

        return ans
        