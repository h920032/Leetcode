#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def match(root, subRoot):
            if not root or not subRoot: return not root and not subRoot
            return root.val == subRoot.val and match(root.left, subRoot.left) and match(root.right, subRoot.right)
        if not root or not subRoot: return not root and not subRoot
        return match(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

# Markle Hash
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def markle(node):
            if not node:
                return "#"
            l = markle(node.left)
            r = markle(node.right)
            node.markle = str(hash(l + str(node.val)+ r))
            return node.markle
        hash_r = markle(root)
        hash_s = markle(subRoot)
        def dfs(root):
            if not root: return hash_s == '#'
            if root.markle == hash_s:
                return True
            return dfs(root.left) or dfs(root.right)
        return dfs(root)

# @lc code=end

