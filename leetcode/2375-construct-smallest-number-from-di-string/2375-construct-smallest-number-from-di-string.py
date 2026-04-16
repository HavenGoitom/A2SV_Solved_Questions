class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = []
        res = ""
        i = 1

        for c in pattern:
            stack.append(i)

            if c == 'I':
                while stack:
                    res += str(stack.pop()) 
            i += 1
            
        stack.append(i)
        while stack:
            res += str(stack.pop())
        
        return res