class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        stack = [] 
        min_i = nums[0]  
        
        for num in nums[1:]:
            while stack and num >= stack[-1][1]:
                stack.pop()  

            if stack and stack[-1][0] < num < stack[-1][1]:
                return True
            
            stack.append((min_i, num))
            
            min_i = min(min_i, num)
        
        return False