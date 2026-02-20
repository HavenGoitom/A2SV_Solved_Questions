class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        nums_sorted = sorted(nums)
        hash_map = {}

        for idx,value in enumerate(nums_sorted):
            if value not in hash_map:
                hash_map[value] = idx
        print(hash_map)

        for i in range(len(nums)):
            nums[i] = hash_map[nums[i]]
        
        return nums

