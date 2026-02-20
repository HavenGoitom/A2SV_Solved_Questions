class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        nums_str = []
        for num in nums:
            nums_str.append(str(num))

        for i in range(len(nums_str)):
            j = i
            while j > 0:
                opt1 = int(nums_str[j-1] + nums_str[j])
                opt2 = int(nums_str[j] + nums_str[j-1])

                if opt1 > opt2:
                    break
                
                nums_str[j-1],nums_str[j] = nums_str[j],nums_str[j-1]
                
                j -= 1

        if nums_str[0] == '0':
            return '0'

        return "".join(nums_str)
