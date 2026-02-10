from collections import Counter

class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        s_counter = Counter(s)
        t_counter = Counter(t)
        missing = 0

        for key in s_counter.keys():
            if s_counter[key] > t_counter[key]:
                missing +=  s_counter[key] - t_counter[key]
        return missing




        