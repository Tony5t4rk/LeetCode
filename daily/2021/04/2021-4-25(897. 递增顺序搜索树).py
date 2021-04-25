# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    pre_node = None

    def dfs(self, cur: TreeNode):
        if cur is None:
            return
        self.dfs(cur.left)
        self.pre_node.right = cur
        self.pre_node.left = None
        cur.left = None
        self.pre_node = cur
        self.dfs(cur.right)

    def increasingBST(self, root: TreeNode) -> TreeNode:
        dummy_node = TreeNode()
        self.pre_node = dummy_node
        self.dfs(root)
        return dummy_node.right