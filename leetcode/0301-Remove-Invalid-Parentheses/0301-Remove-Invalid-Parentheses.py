class Solution:
    def removeInvalidParentheses(self, s: str):
        
        def isvalid(s):
            count = 0

            for c in s:
                if c == '(':
                    count += 1
                elif c == ')':
                    count -= 1
                    if count < 0: #this is saying i say a close bracket before an open one
                        return False # we use this for cases like this ')('
            
            return count == 0
        
        
        level = {s}
        

        while True:

            ans = []

            for s in level:
                if isvalid(s):
                    ans.append(s)

            if ans:
                break
            
            new_level = set()
                    
            for st in level:
                for i in range(len(st)):
                    if st[i] == '(' or st[i] == ')':
                        new_s = st[:i] + st[i+1:]
                        new_level.add(new_s)

            level = new_level
        
        return ans