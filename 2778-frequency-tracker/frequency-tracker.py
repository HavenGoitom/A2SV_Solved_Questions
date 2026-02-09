from collections import defaultdict
class FrequencyTracker(object):
    def __init__(self):
        self.num = defaultdict(int)
        self.freq = defaultdict(int)

    def add(self, number):
        """
        :type number: int
        :rtype: None
        """
        old_value = self.num[number]

        self.num[number] += 1
        if self.freq[old_value] > 0:
            self.freq[old_value] -= 1

        self.freq[self.num[number]] += 1
  

    def deleteOne(self, number):
        """
        :type number: int
        :rtype: None
        """
        old_value = self.num[number]
        if self.num[number] > 0:
            self.num[number] -= 1
            self.freq[old_value] -= 1

            if self.num[number] > 0:
                self.freq[self.num[number]] += 1
        

    def hasFrequency(self, frequency):
        """
        :type frequency: int
        :rtype: bool
        """

        if self.freq[frequency] > 0:
            return True
        return False
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)