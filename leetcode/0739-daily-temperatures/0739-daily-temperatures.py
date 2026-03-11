class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        values = defaultdict(int)
        stack = []
        res = []

        for i in range(len(temperatures)):

            while stack and temperatures[i] > temperatures[stack[-1]]:

                values[stack[-1]] = i-stack[-1]
                stack.pop()

            stack.append(i)
        # print(stack)
        # print(values)
        for i in range(len(temperatures)):
            res.append(values[i])
        return res
        
