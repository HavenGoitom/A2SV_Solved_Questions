class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        idx = [0] * len(nums)

        for i,j in requests:
            idx[i] += 1
            if j < len(nums)-1:
                idx[j+1] -= 1
        
        for i in range(1,len(idx)):
            idx[i] += idx[i-1]

        idx_map = {}

        for i,k in enumerate(idx):
            idx_map[i] = k
        
        print(idx_map)
        sorted_items = sorted(idx_map.items(), key=lambda item: item[1], reverse=True)

        sorted_idx = dict(sorted_items)
       
        num_sorted = sorted(nums, reverse=True)
        print(idx_map)

        i = 0
        ans = [0] * len(nums)

        for k in sorted_idx.keys():
            if i < len(num_sorted):
                ans[k] = num_sorted[i]
                i += 1
        
        for i in range(1,len(ans)):
            ans[i] += ans[i-1]
        print(ans)
        
        total = 0

        for l,r in requests:

            if l == 0:
                total += ans[r]
            else:
                total += ans[r] - ans[l-1]
            
        
        return total % (10**9 +7)
