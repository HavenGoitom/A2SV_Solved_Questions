class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        pattern_word = {}
        word_pattern = {}

        s = list(s.split(" "))

        if len(s) != len(pattern):
            return False

        i = 0

        for word in s:

            if pattern[i] in pattern_word and pattern_word[pattern[i]] != word:
                return False
            
            if word in word_pattern and word_pattern[word] != pattern[i]:
                return False
        
            word_pattern[word] = pattern[i]
            pattern_word[pattern[i]] = word
            i += 1

        return True