# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 0
    _low = 0
    _high = 0

    def dfs(self, cur: TreeNode):
        if cur is None:
            return
        if self._low <= cur.val <= self._high:
            self.ans += cur.val
        if cur.val >= self._low:
            self.dfs(cur.left)
        if cur.val <= self._high:
            self.dfs(cur.right)

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self._low = low
        self._high = high
        self.dfs(root)
        return self.ans