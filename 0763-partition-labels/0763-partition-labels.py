class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        last_idx_map = {}

        for i in range(len(s)):
            last_idx_map[s[i]] = i

        # print(last_idx_map)

        end = 0
        size = 0
        res = []
        i = 0

        while i < len(s):

            size += 1
            end = max(end, last_idx_map[s[i]])

            if i == end:
                res.append(size)
                size = 0
        
            i += 1
        return res