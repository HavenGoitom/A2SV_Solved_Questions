class Solution:
    def hIndex(self, citations: List[int]) -> int:
        res = float('-inf')

        def check(h):
            count = 0
            for c in citations:
                if c >= h:
                    count += 1
            return count >= h
        
        l = 0
        r = len(citations)

        while l <= r:
            h = (l + r) // 2
            if check(h):
                res = max(res, h)
                l = h + 1
            else:
                r = h - 1

        return res
