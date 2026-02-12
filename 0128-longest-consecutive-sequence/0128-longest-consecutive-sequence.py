from collections import Counter

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # [100,4,200,1,3,2]
        # [0,3,7,2,5,8,4,6,0,1]
        # [1,2,0,1]
        # [0]
        # [0,0]
        # [] 
        # You can set it to remove duplicates and use pointer to find the elemnts.
        # But try to think of a way to use hashtables.

        nums_sort = sorted(nums)
        nums_map = Counter(nums_sort) 
        nums_map = sorted(nums_map.items())
        print(nums_map)

        max_len = 0
        count = 0

        if len(nums_map) == 1:
            return 1

        for key, value in nums_map:

            if count == 0:
                previous = key
                count += 1
                max_len = max(max_len,count)
                
            elif value > 0 and key == previous + 1:
                count += 1                
                previous = key
                max_len = max(max_len,count)
            elif value > 0:
                count = 1
                previous = key

        return max_len
                    


            