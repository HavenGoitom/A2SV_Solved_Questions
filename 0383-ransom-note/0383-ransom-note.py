from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        ransomNote_table = Counter(ransomNote)
        magazine_table = Counter(magazine)

        for key in ransomNote_table:
            if ransomNote_table[key] >  magazine_table[key]:
                return False
        
        return True