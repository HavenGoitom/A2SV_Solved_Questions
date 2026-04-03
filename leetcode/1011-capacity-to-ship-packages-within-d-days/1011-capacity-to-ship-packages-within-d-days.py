class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights) #lower bound
        right = sum(weights) #upper bound
        res = float('inf')

        def canHold(capa):
            ships = 1
            currWeight = 0
            for weight in weights:
                if currWeight + weight > capa:
                    ships += 1
                    currWeight = 0
                currWeight += weight
            return ships <= days


        while left <= right:
            capa = (left + right) // 2
            
            if canHold(capa):
                res = min(res, capa)
                right = capa - 1
            else:
                left = capa + 1

        return res
            


