class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        left = 0
        right = k
        windowSum = 0
        for i in range(k):
            windowSum += nums[i]
        max_avg = windowSum/float(k)

        while right<len(nums):
            windowSum = windowSum - nums[left] + nums[right]
            if windowSum/float(k) > max_avg:
                max_avg = windowSum/float(k)
            left += 1
            right +=1
        return max_avg

            