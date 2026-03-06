# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        curr = dummy
        count = 0
        
        while curr:
            count +=1
            curr = curr.next
       # print(count)
        i = 0
        count -= 1
        curr = dummy

        if count == 1:
            return head

        while curr and curr.next:
            i += 1
            if i == (count // 2):
                return curr.next.next

            curr = curr.next



