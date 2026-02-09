class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        s_list = list(s)
        res = [''] * len(s_list)
        for i in range(len(s_list)):
            res[indices[i]] = s_list[i]
        return "".join(res)
