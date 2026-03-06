class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        prefix_sum = 0
        min_val = 0

        for num in nums:
            prefix_sum += num
            min_val = min(min_val, prefix_sum)

        return 1 - min_val
