class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        def merge(nums1, nums2):
            merged = []
            i,j = 0,0
            while i < m and j < n:
                if nums1[i] < nums2[j]:
                    merged.append(nums1[i])
                    i += 1
                else:
                    merged.append(nums2[j])
                    j += 1

            merged.extend(nums1[i:])
            merged.extend(nums2[j:])
            return merged
        
        merged_num = merge(nums1, nums2)
        if len(merged_num) % 2 == 1:
            mid = len(merged_num)//2
            return merged_num[mid]
        else:
            mid1 = len(merged_num) // 2
            mid2 = mid1 - 1
            ans = merged_num[mid1] + merged_num[mid2]
            return ans / 2

        # m = len(nums1)
        # n = len(nums2)
        # nums = nums1 + nums2
        # nums.sort()

        # if (m + n) % 2 == 1:
        #     mid = (m + n)//2
        #     return nums[mid]
        # else:
        #     mid1 = (m + n) // 2
        #     mid2 = mid1 - 1
        #     ans = nums[mid1] + nums[mid2]
        #     return ans / 2

