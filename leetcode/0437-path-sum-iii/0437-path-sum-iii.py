# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.paths = 0

        def target(node, currSum):
            if not node:
                return
            currSum += node.val

            if currSum == targetSum:
                self.paths += 1

            target(node.left, currSum)
            target(node.right, currSum)
        
        def dfs(node):
            if not node:
                return
            target(node, 0)
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return self.paths