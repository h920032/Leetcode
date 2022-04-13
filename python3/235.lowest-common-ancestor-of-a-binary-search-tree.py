#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if q.val < p.val: return self.lowestCommonAncestor(root, q, p)
        def dfs(root):
            if (p.val < root.val and q.val > root.val) or p.val == root.val or q.val == root.val: return root
            if p.val > root.val and q.val > root.val: return dfs(root.right)
            if p.val < root.val and q.val < root.val: return dfs(root.left)
        return dfs(root)
               
# @lc code=end

