class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        weighted_ord = {}
        s = list(s)

        for i in range(len(order)):
             weighted_ord[order[i]] = i

        s.sort(key = lambda char: weighted_ord.get(char, len(order)))
        
        return "".join(s)

