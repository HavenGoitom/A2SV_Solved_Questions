class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        prefix_idx = {0:1}
        total = 0
        count = 0

        for idx,num in enumerate(nums):
            total += num
            val = total % k

            if val in prefix_idx:
                count += prefix_idx[val]
                prefix_idx[val] += 1
            else:
                prefix_idx[val] = 1
        return count

