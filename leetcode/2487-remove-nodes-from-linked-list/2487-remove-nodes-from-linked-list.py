# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        
        def decreMono(curr):
            
            if not curr or not curr.next:
                return curr
            
            next_node = decreMono(curr.next)
            curr.next = next_node

            if curr.val >= next_node.val:
                return curr
            else:
                return next_node
        
        return decreMono(curr)

        # stack = []
        # current = head
        # while current:
        #     stack.append(current)
        #     current = current.next

        # current = stack.pop()
        # maximum = current.val
        # result_list = ListNode(maximum)
        
        # while stack:
        #     current = stack.pop()
        #     if current.val < maximum:
        #         continue
        #     else:
        #         new_node = ListNode(current.val)
        #         new_node.next = result_list
        #         result_list = new_node
        #         maximum = current.val
                
        # return result_list

