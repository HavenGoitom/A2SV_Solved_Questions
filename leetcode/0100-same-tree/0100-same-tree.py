# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res_p = []
        res_q = []

        def bfs(node, ans):
            if not node:
                ans.append(None)
                return
            ans.append(node.val)
            bfs(node.left,ans)
            bfs(node.right, ans)

        bfs(p, res_p)
        bfs(q, res_q)

        return res_p == res_q