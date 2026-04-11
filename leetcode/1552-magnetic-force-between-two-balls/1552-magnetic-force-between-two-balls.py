class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        ans = 0

        def canPut(dist):
            count = 1
            first = position[0]
            for i in range(1, len(position)):
                if position[i] >= first + dist: #is it far enough from the first ball
                    count += 1
                    first = position[i]
            return count >= m


        left = 1 #min distance
        right = position[-1] - position[0] #max distance

        while left <= right:
            dist = (left + right) // 2

            if canPut(dist):
                ans = max(ans, dist)
                left = dist + 1
            else:
                right = dist - 1
        
        return ans    