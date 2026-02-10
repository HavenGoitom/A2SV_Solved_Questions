from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = Counter(s)
        t_counter = Counter(t)

        if len(s)>len(t):
            return False

        for key in t_counter:
            if t_counter[key] != s_counter[key]:
                return False
        return True
