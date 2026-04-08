class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        def closest_distance(house):
            left, right = 0, len(heaters) - 1

            while left <= right:
                mid = (left + right) // 2

                if heaters[mid] == house:
                    return 0
                elif heaters[mid] < house:
                    left = mid + 1
                else:
                    right = mid - 1

            dist1 = float('inf')
            dist2 = float('inf')

            if right >= 0:
                dist1 = house - heaters[right]

            if left < len(heaters):
                dist2 = heaters[left] - house

            return min(dist1, dist2)

        result = 0

        for house in houses:
            result = max(result, closest_distance(house))

        return result