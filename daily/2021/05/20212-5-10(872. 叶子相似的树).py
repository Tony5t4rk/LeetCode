# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:

        def dfs(cur):
            if cur.left is None and cur.right is None:
                return [cur.val]
            elif cur.left is None:
                return dfs(cur.right)
            elif cur.right is None:
                return dfs(cur.left)
            return dfs(cur.left) + dfs(cur.right)
        
        return dfs(root1) == dfs(root2)