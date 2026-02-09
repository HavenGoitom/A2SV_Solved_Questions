from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums_counter = Counter(nums)
        sorted_nums = sorted(nums_counter.items(), key = lambda x : x[1], reverse = True)
        nums_value = []
        k_count= 0

        for num in sorted_nums:
            nums_value.append(num[0])
            k_count += 1
            if k == k_count:
                return nums_value
        return nums_value

            
            

        