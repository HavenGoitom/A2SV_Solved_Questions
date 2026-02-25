class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        right = len(people)-1
        left = 0
        count = 0

        while right >= 0:
            if people[right] == limit:
                count += 1
                right -= 1
                continue
            if people[right] + people[left] <= limit:
                right -= 2
                left += 2
                count += 1
                continue
            count += 1
            right -= 1

        return count



            