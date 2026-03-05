class Solution:
    def subarraySum(self, nums, k):
        
        total = 0
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        count = 0

        for num in nums:
            total += num
            
            count += prefix_sum[total - k]
            prefix_sum[total] += 1
        
        # print(nums)
        
        return count
