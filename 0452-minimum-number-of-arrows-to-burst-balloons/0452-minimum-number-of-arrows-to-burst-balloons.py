class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(reverse = True)
        # print(points) [[10, 16], [7, 12], [2, 8], [1, 6]]
        i = 0
        j = 1
        count = 0

        if len(points) == 1:
            return 1

        while i<len(points)-1:
            # print("test") 
            if j == len(points):
                break

            if points[i][0] <= points[j][1]:
                j += 1
                if j == len(points):
                    count += 1
                    i += 1
                continue

            count += 1 

            i = j
            if i == len(points) - 1:
                count += 1
                i += 1
                break
            j += 1
            
        return count