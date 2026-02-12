class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        top = 0
        left = 0
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1

        result = []

        while top <= bottom and left <= right:

            # Traverse top row (left → right)
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1  # Move top boundary down

            # Traverse right column (top → bottom)
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1  # Move right boundary left

            # Traverse bottom row (right → left), if rows remain
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1  # Move bottom boundary up

            # Traverse left column (bottom → top), if columns remain
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1  # Move left boundary right

        return result
