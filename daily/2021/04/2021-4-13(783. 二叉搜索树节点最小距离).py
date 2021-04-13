# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.min_diff = float('inf')
        self.pre = None
        def dfs(cur):
            if cur.left:
                dfs(cur.left)
            if not self.pre is None:
                self.min_diff = min(self.min_diff, cur.val - self.pre.val)
            self.pre = cur
            if cur.right:
                dfs(cur.right)
        dfs(root)
        return self.min_diff