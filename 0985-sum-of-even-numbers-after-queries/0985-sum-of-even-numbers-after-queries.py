class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        hash_map = {}
        sum_of_nums = 0

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                hash_map[i] = nums[i]
                sum_of_nums += nums[i]
        # print(hash_map,sum_of_nums)
        res = []

        for val,idx in queries:
            nums[idx] += val

            if idx not in hash_map and nums[idx] % 2 == 0:
                sum_of_nums += nums[idx]
                hash_map[idx] = nums[idx]

            elif idx in hash_map:
                old_val = hash_map[idx] 

                if nums[idx] % 2 == 0:
                    sum_of_nums += val
                    hash_map[idx] = nums[idx]
                else:
                    sum_of_nums -= old_val
                    del hash_map[idx]

            res.append(sum_of_nums)
            
        return res
