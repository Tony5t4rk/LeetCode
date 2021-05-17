# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        father, depth = {x: None, y: None}, {x: 0, y: 0}
        
        def dfs(cur: TreeNode, pre: TreeNode, dep: int):
            if cur is None:
                return
            if cur.val == x:
                father[x] = pre
                depth[x] = dep
            elif cur.val == y:
                father[y] = pre
                depth[y] = dep
            dfs(cur.left, cur, dep + 1)
            dfs(cur.right, cur, dep + 1)
        
        dfs(root, None, 0)
        return depth[x] == depth[y] and father[x] != father[y]