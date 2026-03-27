class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [(i+1) for i in range(n)]
        combination = []
        # print(nums)

        def backtracking(idx,combined):

            if len(combined) == k:
                combination.append(combined[:])
                return

            for i in range(idx, n):

                combined.append(nums[i])
                backtracking(i + 1 ,combined)
                combined.pop()

        backtracking(0,[])

        return combination