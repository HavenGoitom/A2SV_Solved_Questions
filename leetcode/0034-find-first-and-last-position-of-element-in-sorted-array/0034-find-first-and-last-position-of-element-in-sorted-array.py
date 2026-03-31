class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        ans = []

        def findFirst(nums, target):
            left = 0
            right = len(nums) - 1

            while left <= right:
                mid = (right + left) // 2

                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return left
        
        first = findFirst(nums, target)
        if first == len(nums) or nums[first] != target:
            return [-1, -1]

        last = findFirst(nums, target + 1) - 1
        return [first,last]