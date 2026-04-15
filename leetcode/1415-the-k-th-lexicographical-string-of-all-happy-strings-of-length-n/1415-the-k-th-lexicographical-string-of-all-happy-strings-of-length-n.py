class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []

        def helper(letter):
            if len(res) == k:
                return

            if len(letter) == n:
                res.append("".join(letter))
                return 
            
            if letter[-1] == 'a':
                letter.append('b')
                helper(letter)
                letter.pop()

                letter.append('c')
                helper(letter)
                letter.pop()
            elif letter[-1] == 'b':
                letter.append('a')
                helper(letter)
                letter.pop()

                letter.append('c')
                helper(letter)
                letter.pop()
            else:
                letter.append('a')
                helper(letter)
                letter.pop()

                letter.append('b')
                helper(letter)
                letter.pop()
        
        for chr in "abc":
            helper([chr])

        if k > len(res):
            return ""
        # print(res, res[k-1])
        return res[k-1]