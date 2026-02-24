class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if needle not in haystack:
            return -1
        
        for i in range(len(haystack)):
            right = 0

            while right < len(needle) and haystack[right+i] == needle[right]:
                right += 1
                
            if right == len(needle):
                return i
                