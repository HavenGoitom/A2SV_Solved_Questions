class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        nums = nums1 + nums2
        nums.sort()

        if (m + n) % 2 == 1:
            mid = (m + n)//2
            return nums[mid]
        else:
            mid1 = (m + n) // 2
            mid2 = mid1 - 1
            ans = nums[mid1] + nums[mid2]
            return ans / 2

