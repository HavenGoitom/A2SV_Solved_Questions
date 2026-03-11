class ListNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:
    def __init__(self, homepage: str):
        self.homepage = homepage
        self.curr = ListNode(homepage)    
    
    def visit(self, url: str) -> None:
        self.new_node = ListNode(url)
        self.curr.next = self.new_node
        self.new_node.prev = self.curr

        self.curr = self.curr.next
        

    def back(self, steps: int) -> str:

        while (self.curr and self.curr.prev) and steps > 0:
            self.curr = self.curr.prev
            steps -= 1

        return self.curr.val

    def forward(self, steps: int) -> str:
        
        while (self.curr and self.curr.next) and steps > 0:
            self.curr = self.curr.next
            steps -= 1

        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)