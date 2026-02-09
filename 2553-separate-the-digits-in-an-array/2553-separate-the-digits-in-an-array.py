class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        for num in nums:
            for each_num in str(num):
                output.append(int(each_num))
        return output
