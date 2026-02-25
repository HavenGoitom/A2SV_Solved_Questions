class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        left,right = 0,k
        total = sum(nums[left:right])
        average = total / k


        for i in range(len(nums)-k):
            
            total += nums[right]
            total -= nums[left] 

            average = max(average, total/k)

            right += 1
            left += 1
        
        return average