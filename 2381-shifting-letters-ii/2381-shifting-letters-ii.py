class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        prefix_sum = [0]*(len(s)+1)

        for l,r,d in shifts:
            if d == 0:
                prefix_sum[l] += -1
                prefix_sum[r+1] += 1
            else:
                prefix_sum[l] += 1
                prefix_sum[r+1] += -1
        
        print(prefix_sum)
        total = 0

        for i in range(len(prefix_sum)):
            total += prefix_sum[i]
            prefix_sum[i] = total
        
        print(prefix_sum)
        s = list(s)

        for i in range(len(s)):
            s[i] = chr(ord("a") + (((ord(s[i]) + prefix_sum[i]) -  ord("a")) % 26))#122+1-97 = 26
        
        return "".join(s)
