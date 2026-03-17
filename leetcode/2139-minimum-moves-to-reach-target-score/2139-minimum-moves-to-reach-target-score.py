class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        
        ans_of_the_div = []
        moves = 0
        div = target
        n = 0

        if maxDoubles == 0:
            return target - 1

        while maxDoubles > 0 and div != 1:
            div = div // 2
            ans_of_the_div.append(div)
            maxDoubles -= 1
            n += 1
        
        # print(ans_of_the_div)
        # print(target)

        if ans_of_the_div:
            moves += (ans_of_the_div[-1] - 1)
        
        for i in range(n):
            multi = ans_of_the_div.pop() * 2
            moves += 1 
            # print(multi)

            if not ans_of_the_div:
                moves += (target - multi)
                break
            moves += (ans_of_the_div[-1] - multi)

        return moves