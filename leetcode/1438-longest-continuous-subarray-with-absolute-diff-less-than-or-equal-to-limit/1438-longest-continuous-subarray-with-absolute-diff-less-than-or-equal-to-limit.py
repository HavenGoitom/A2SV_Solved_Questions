class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_queue = deque() #decreasing 
        min_queue = deque() # increasing
        l = 0
        ans = 0

        for r in range(len(nums)):
            while max_queue and nums[r] > max_queue[-1]:
                max_queue.pop()
            #max monotonicity
            while min_queue and nums[r] < min_queue[-1]:
                min_queue.pop()
            #min monotonicity
            max_queue.append(nums[r])
            min_queue.append(nums[r])

            while max_queue[0] - min_queue[0] > limit:
                if max_queue[0] == nums[l]:
                    max_queue.popleft()
            
                if min_queue[0] == nums[l]:
                    min_queue.popleft()

                l += 1
            
            ans = max(ans, r - l + 1)
        
        return ans
            