class Solution:
    def removeStars(self, s: str) -> str:
        
        stack = []
        for char in s:
            if char == '*':
                if stack:
                    stack.pop()
                else:
                    return ""
            else:
                stack.append(char)

        return "".join(stack)
