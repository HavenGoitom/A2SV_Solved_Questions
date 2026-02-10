import random
class RandomizedSet:

    def __init__(self):
        self.num_dict = {}
        self.value = []

    def insert(self, val: int) -> bool:
        if val not in self.num_dict:
            self.num_dict[val] = len(self.num_dict)
            self.value.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.num_dict:
            if val == self.value[-1]:
                self.value.pop()
            else:
                # 1 2 3
                self.num_dict[self.value[-1]] = self.num_dict[val] # update the idx in dict
                self.value[self.num_dict[val]] = self.value[-1] # move it to the back 1 3 3
                self.value.pop() # 1 3 so 2 is deleted

            del self.num_dict[val]
            return True
        return False
    def getRandom(self) -> int:
        return random.choice(self.value)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
