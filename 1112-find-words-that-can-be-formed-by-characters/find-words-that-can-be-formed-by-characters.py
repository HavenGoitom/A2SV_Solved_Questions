from collections import Counter

class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        chars_dict = Counter(chars)

        count = 0

        for w in words:
            w_dict = Counter(w)        
            flag = True
            for key in w_dict:
                if key not in chars_dict.keys() or chars_dict[key] < w_dict[key] :
                    flag = False
                    break
            if flag:
                count += len(w)

        
        return count


                