# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1,head)
        curr = dummy

        i = 0
        count = 0
        while curr:
            curr = curr.next
            count += 1
        n = count - n 

        curr = dummy

        while curr and curr.next:

            if i == n-1:
                curr.next = curr.next.next
                break

            curr = curr.next                
            i += 1

        return dummy.next