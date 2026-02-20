class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
    # a+b>c for the triangle to be formed
    
        nums.sort(reverse = True)
        # 10 2 1 1
        for i in range(len(nums)-2):
            print(i)
            if nums[i+1] + nums[i+2] > nums[i]:
                return nums[i] + nums[i+1] + nums[i+2]
        
        return 0
