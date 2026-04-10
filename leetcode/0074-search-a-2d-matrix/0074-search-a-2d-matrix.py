class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1

        while left <= right:
            mid = (left + right) // 2
            l = 0
            r = len(matrix[mid]) - 1

            if target < matrix[mid][0]:
                right = mid - 1
            elif target > matrix[mid][-1]:
                left = mid + 1
            else:
                while l <= r:

                    mid_inside = (l + r) // 2

                    if matrix[mid][mid_inside] == target:
                        return True
                    elif target > matrix[mid][mid_inside]:
                        l = mid_inside + 1
                    else:
                        r = mid_inside - 1
                return False
            
        return False
                    
                    

