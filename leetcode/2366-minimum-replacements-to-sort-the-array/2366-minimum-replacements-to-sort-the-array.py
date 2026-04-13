class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        # the greedy part here is we are trying to maximize the left element of the split
        count = 0
        right = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            left = nums[i]

            if left > right:
                count += (math.ceil(left/right) - 1) # decrease itself since we dont count it
                right = left // (math.ceil(left/right))
            else:
                right = left
        
        return count