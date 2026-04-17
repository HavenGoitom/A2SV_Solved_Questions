class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total = n*(n+1)//2
        mytotal = sum(nums)
        unique_sum = sum(set(nums))
        
        duplicate = mytotal - unique_sum
        missing = total - unique_sum 

        return [duplicate, missing]