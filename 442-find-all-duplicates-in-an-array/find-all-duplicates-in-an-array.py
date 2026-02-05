from collections import Counter

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        nums_dict = Counter(nums)

        output = []

        for key in nums_dict:
            if nums_dict[key] > 1:
                output.append(key)
        
        return output