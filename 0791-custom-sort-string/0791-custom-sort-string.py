class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        weighted_ord = {}
        s = list(s)

        for i in range(len(order)):
             weighted_ord[order[i]] = i

        for i in range(len(s)):
            for j in range(len(s)-1-i):
                if weighted_ord.get(s[j+1], len(s)) < weighted_ord.get(s[j], len(s)):
                    s[j+1], s[j] = s[j], s[j+1]
            print(s)
        return "".join(s)

