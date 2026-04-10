class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        ans = float('inf')
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[left] <= nums[right]:
                ans = min(ans, nums[left])
                break
            
            ans = min(ans, nums[mid])
            
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        
        return ans