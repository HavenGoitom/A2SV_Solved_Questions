class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def helper(idx, subseq, pre):
            if idx == len(nums):
                if len(subseq) > 1:
                    if subseq not in ans:
                        ans.append(subseq.copy())
                return
            
            if nums[idx] >= pre:
                pre_2 = nums[idx]
                subseq.append(pre_2)
                helper(idx + 1, subseq,pre_2)
                subseq.pop()
            helper(idx + 1, subseq,pre)
        
        helper(0, [], -100)
    
        return ans