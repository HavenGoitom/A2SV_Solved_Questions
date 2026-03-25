# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        self.depth = 10**5   
        
        def dfs(node,count):
        
            if not node:
                return
                
            if not node.left and not node.right:
                self.depth = min(self.depth, count)
                return

            dfs(node.left, count + 1)
            dfs(node.right, count + 1)

        dfs(root,1)

        return self.depth

            
