class Solution:
    def smallestPalindrome(self, s: str) -> str:
        
        hash_map = Counter(s)

        keys = list(hash_map.keys())
        set_s = sorted(keys)
        # print(set_s)

        res = []
        str1 = []
        str2 = []
        collect = ""
        i = 0

        while i<len(set_s):
            if hash_map[set_s[i]] % 2 == 0:
                # print(set_s[i])
                val = hash_map[set_s[i]]//2
                str1.extend(list(set_s[i] * val)) #aa
                str2.extend(list(set_s[i] * val ))
    
                i += 1

            else:
                val = hash_map[set_s[i]]//2
                if val >= 1:
                    str1.extend(list(set_s[i] * val))
                    str2.extend(list(set_s[i] * val))

                collect = set_s[i]
                i += 1

        if collect:
            str1.append(collect)
        
        res = str1 + str2[::-1]
        
        # if ans == ans[::-1]:
        return "".join(res)
        # return s


