class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        count_of_zeros = 0
        max_len = 0
        left = 0

        for right in range(len(nums)):

            if nums[right] == 0:
                count_of_zeros += 1
            
            while count_of_zeros == 2:
                if nums[left] == 0:
                    count_of_zeros -= 1
                left += 1
            
            max_len = max(max_len, (right - left))

        return max_len