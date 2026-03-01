from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def at_most(nums, k):

            freq = defaultdict(int)
            unique = 0
            count = 0
            left = 0

            for right in range(len(nums)):

                if freq[nums[right]] == 0:
                    unique += 1

                freq[nums[right]] += 1

                while unique > k:

                    freq[nums[left]] -= 1

                    if freq[nums[left]] == 0:
                        unique -= 1
                    left += 1

                count += (right - left + 1)

            return count

        a = at_most(nums,k)
        b = at_most(nums,k-1)

        return a-b
