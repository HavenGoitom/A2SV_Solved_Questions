class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # for i in range(n):
        #     for j in range(n-1):
        #         if nums[j] > nums[j + 1]:
        #             nums[j], nums[j + 1] = nums[j + 1], nums[j]

        zero = 0
        one = 0
        two = 0

        for i in range(n):
            if nums[i] == 0:
                zero +=1
            elif nums[i] == 1:
                one += 1
            else: 
                two += 1
        
        j = 0

        while j < n:
            if zero > 0:
                nums[j] = 0
                zero -= 1
                j += 1
                continue
            if one > 0:
                nums[j] = 1
                one -= 1
                j += 1
                continue
            if two > 0:
                nums[j] = 2
                two -= 1
                j += 1
        
                