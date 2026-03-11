class DataStream:

    def __init__(self, value: int, k: int):
        self.queue = deque()
        self.count = 0
        self.value = value
        self.k = k

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.queue.append(num)
        else:
            while self.queue:
                self.queue.popleft()
        if len(self.queue) >= self.k:
            return True
        return False


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)