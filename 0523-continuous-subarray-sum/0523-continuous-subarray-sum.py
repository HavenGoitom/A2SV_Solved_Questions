class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        total = 0

        #so if two nums divided by k remainder is the same then the two nums difference will give us a number who is divisibel by k
        
        # print(nums)
        hash_map = {0: -1}
        total = 0

        for i in range(len(nums)):
            total += nums[i]
            val = total % k

            if val in hash_map and i - hash_map[val] >= 2:
                return True
            elif val not in hash_map:
                hash_map[val] = i
        
        return False

        # print(nums)
        # print(hash_map)
            



