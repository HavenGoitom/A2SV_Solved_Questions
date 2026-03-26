class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s)< 2:
            return ""

        set_s = set(s)

        for i,v in enumerate(s):
            if v.swapcase() not in set_s:
                s_left = self.longestNiceSubstring(s[:i])
                s_right = self.longestNiceSubstring(s[i+1:])

                if len(s_left) >= len(s_right):
                    return s_left
                else:
                    return s_right

        return s
                


