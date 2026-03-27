class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtracking(idx, subset):
            if idx == len(nums):
                result.append(subset.copy())
                return 
            
            subset.append(nums[idx])
            backtracking(idx + 1, subset)
            subset.pop()

            backtracking(idx + 1, subset)
            # automatically ends when it finishes so auto return
        backtracking(0, [])

        return result