from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        if set(word1) != set(word2):
            return False
        
        word1_count = Counter(word1)
        word2_count = Counter(word2)

        sorted_word1 = sorted(word1_count.values())
        sorted_word2 = sorted(word2_count.values())

        if sorted_word1 != sorted_word2:
            return False
        return True