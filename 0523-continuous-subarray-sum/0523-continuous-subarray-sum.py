class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        total = 0

        #so if two nums divided by k remainder is the same then the two nums difference will give us a number who is divisibel by k

        for i in range(len(nums)):
            total += nums[i]
            nums[i] = total
        
        # print(nums)
        hash_map = defaultdict(int)
        hash_map[0] = 1

        for i in range(len(nums)):
            val = nums[i] % k

            if hash_map[val] and (i+2) - hash_map[val] >= 2:
                return True
            elif hash_map[val] == 0:
                hash_map[val] = i+2
        
        return False

        # print(nums)
        # print(hash_map)
            



