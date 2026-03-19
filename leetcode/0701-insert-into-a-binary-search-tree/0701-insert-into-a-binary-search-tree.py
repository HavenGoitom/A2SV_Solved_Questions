# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        val_node = TreeNode(val)
        
        def helper(node, root):
            if not root:
                return node
            if node.val < root.val:
                root.left = helper(node, root.left)
            else:
                root.right = helper(node, root.right)
                
            return root

        return helper(val_node, root)
