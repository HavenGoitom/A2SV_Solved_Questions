class Solution:
    def frequencySort(self, s: str) -> str:
        s_dict = {}
        output = []

        for char in set(s):
            if s.count(char) not in s_dict:
                s_dict[s.count(char)] = [char]
            else: 
                s_dict[s.count(char)].append(char)
        
        keys = sorted(list(s_dict.keys()))
        n = len(keys)

        for i in range(n):
            max_len = keys[-1]
            letters = s_dict[max_len]

            for letter in letters:
                word = letter * max_len
                output.append(word) 

            keys.pop()
            
        return "".join(output)