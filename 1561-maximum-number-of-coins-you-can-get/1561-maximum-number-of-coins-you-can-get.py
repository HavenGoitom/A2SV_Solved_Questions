class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # 9 8 7 6 5 4 3 2 1
        # 8 + 6 + 4
        piles.sort(reverse = True)

        sum_pile = 0
        add = 1

        for i in range(len(piles)//3):

            sum_pile += piles[add]
            add += 2
        
        return sum_pile