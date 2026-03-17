class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
         
        freq = {}

        for idx, cities in enumerate(costs):
            freq[idx] = cities[0] - cities[1]

        order = sorted(freq, key=lambda x: freq[x])

        n = len(costs)
        total = 0

        for i in range(n//2):
            total += costs[order[i]][0]

        for i in range(n//2, n):
            total += costs[order[i]][1]

        return total