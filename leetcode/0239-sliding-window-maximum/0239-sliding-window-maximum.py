class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        left = 0
        res = []

        for i in range(len(nums)):
            while queue and queue[-1] < nums[i]:
                queue.pop()
            queue.append(nums[i])
                
            if i - left  == k-1:
                res.append(queue[0])
                if queue[0] == nums[left]:
                    queue.popleft()
                left += 1
        return res

