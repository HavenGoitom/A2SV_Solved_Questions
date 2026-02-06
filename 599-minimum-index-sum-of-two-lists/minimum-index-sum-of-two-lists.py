from collections import Counter

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        list1_counter = Counter(list1)
        list2_counter = Counter(list2)

        min_index = 2000000

        for word in list1:
            if list2_counter[word]>0:
                min_index = min(min_index,list1.index(word)+list2.index(word))

        result = []

        for word in list1:
            if list2_counter[word] > 0:
                if list1.index(word) + list2.index(word) == min_index:
                    result.append(word)


        return result
