# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
            self.total = 0

    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        
        def helper(node, parent, grandparent):

            if not node:
                return
            
            if grandparent and grandparent.val % 2 == 0:
                self.total += node.val

            helper(node.left, node, parent)
            helper(node.right, node, parent)

        helper(root,None,None)  
        
        return self.total
            
