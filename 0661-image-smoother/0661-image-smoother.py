class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:

        m = len(img)
        n = len(img[0])

        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 0),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]

        img_smoothed = [[0] * n for i in range(m)]

        # print(img_smoothed)

        for i in range(m):
            for j in range(n):
                sum_nums = 0
                count = 0

                for d1, d2 in directions:
                    if i + d1 >= 0 and i + d1 < m and j + d2 >= 0 and j + d2 < n:
                        sum_nums += img[i + d1][j + d2]
                        count += 1

                img_smoothed[i][j] = floor(sum_nums / count)
                # print(img[i][j])

        return img_smoothed
