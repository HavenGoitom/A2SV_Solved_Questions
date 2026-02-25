class Solution:
    def subarraySum(self, nums, k):
        count = 0
        currentSum = 0
        prefixCount = {0: 1}  

        for num in nums:
            currentSum += num

            if currentSum - k in prefixCount:
                count += prefixCount[currentSum - k]

            prefixCount[currentSum] = prefixCount.get(currentSum, 0) + 1

        return count