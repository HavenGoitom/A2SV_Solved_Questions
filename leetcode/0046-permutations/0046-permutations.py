class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtracking(idx, perm):
            if len(perm) == len(nums):
                res.append(perm[:])
                return
                
            for i in range(len(nums)):
                if nums[i] not in perm:
                    perm.append(nums[i])
                    backtracking(i + 1, perm)
                    perm.pop()

        backtracking(0,[])
        
        return res