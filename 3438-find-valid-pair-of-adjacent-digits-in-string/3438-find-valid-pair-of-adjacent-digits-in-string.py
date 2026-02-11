from collections import Counter
class Solution:
    def findValidPair(self, s: str) -> str:

        s_counter = Counter(s)
        output = []

        for i in range(len(s)-1):
            if s_counter[s[i]] == int(s[i]) and s_counter[s[i+1]]==int(s[i+1]) and s[i] != s[i+1]:
                output.extend([s[i],s[i+1]])
                break
        
        return "".join(output)
