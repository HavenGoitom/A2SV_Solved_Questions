class Solution(object):
    def isCovered(self, ranges, left, right):

        for num in range(left, right + 1):
            count = 0
            for r in ranges:
                if r[0] <= num <= r[1]:
                    count += 1
            if count == 0:
                return False
                
        return True
        