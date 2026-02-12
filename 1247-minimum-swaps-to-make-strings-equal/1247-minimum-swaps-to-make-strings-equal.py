class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        
        s3 = s1+s2
        if s3.count('x') % 2 == 1 or s3.count('y') % 2 == 1:
            return -1

        string_zip = list(zip(s1,s2))
        #[('x', 'y'), ('x', 'y')]
        ans = 0
        count_xy = 0
        count_yx = 0

        for pair in string_zip:
            if pair[0] == 'x' and pair[1] == 'y':
                count_xy += 1
            elif pair[0] == 'y' and pair[1] == 'x':
                count_yx += 1
        
        if count_xy % 2 == 0 and count_yx % 2 == 0:
            ans += count_xy//2 + count_yx//2
        else:
            ans += count_xy//2 + count_yx//2 + 2
        
        return ans
            
        