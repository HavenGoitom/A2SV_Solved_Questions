# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def checkSame(node,subRoot):
            if not node and not subRoot:
                return True

            if not node or not subRoot:
                return False

            if node.val != subRoot.val:
                return False
            
            return checkSame(node.left, subRoot.left) and checkSame(node.right, subRoot.right)

        def findSameRoot(node, subRoot):
            if not node:
                return False
            if node.val == subRoot.val and checkSame(node,subRoot):
                return True
            
            return findSameRoot(node.left, subRoot) or findSameRoot(node.right, subRoot)
        
        return findSameRoot(root,subRoot)

