from collections import Counter

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:

        nums_counter = Counter(nums)
        print(nums_counter)
        f = 0

        for key in nums_counter:
            if nums_counter[key] > f:
                f = nums_counter[key]
                x = key
        # print(x,f) x = 1 f = 6

        left = 0
        right = 1

        for i in range(len(nums)):
            nums_split = nums[left:right] #2
            freq_1 = nums_split.count(x) #0
            freq_2 = f-freq_1 #6

            if freq_1 * 2 > len(nums_split) and freq_2 * 2 > len(nums) - len(nums_split):
                return right-1
            
            right += 1

        return -1
            



                