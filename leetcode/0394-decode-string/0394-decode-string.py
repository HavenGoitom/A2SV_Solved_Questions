class Solution:
    def decodeString(self, s: str) -> str:
        res = ""
        k = 0
        stack = []

        for char in s:
            
            if char.isdigit():
                k = k * 10 + int(char)
            elif char == "[":
                stack.append((res, k))
                res = ""
                k = 0
            elif char == "]":
                last_string, last_int = stack.pop()
                res = last_string + (res * last_int)
            else:
                res += char
        return res