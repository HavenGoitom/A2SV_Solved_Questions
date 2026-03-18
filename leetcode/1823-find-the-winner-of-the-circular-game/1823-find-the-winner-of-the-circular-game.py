class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        array = [x for x in range(1,n+1)]

        def helper(i):
            if len(array) == 1:
                return array[0]
            
            deleted_guy = (i + k-1) % len(array)
            array.pop(deleted_guy)
            return helper((deleted_guy) % len(array))
            
        return helper(0)

        # queue = deque()

        # for i in range(1, n+1):
        #     queue.append(i)
        
        # while len(queue) > 1:
        #     for i in range(k-1):
        #         back = queue.popleft()
        #         queue.append(back)
        #     queue.popleft()

        # return queue[0]
