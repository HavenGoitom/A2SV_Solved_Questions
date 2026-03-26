# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(node):
            if not node:
                return [0,0] # size, coins

            left_size, left_coin = dfs(node.left)
            right_size, right_coin = dfs(node.right)

            size = 1 + left_size + right_size
            coins = node.val + left_coin + right_coin

            self.res += abs(size - coins)
            
            return [size, coins]

        dfs(root)

        return self.res