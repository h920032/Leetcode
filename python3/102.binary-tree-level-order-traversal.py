#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = {}
        def dfs(root, n):
            if root:
                if n not in d: d[n] = [root.val]
                else: d[n].append(root.val)
                dfs(root.left, n + 1)
                dfs(root.right, n + 1)
        dfs(root, 0)
        return list(d.values())        
# @lc code=end

