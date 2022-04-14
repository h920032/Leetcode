#
# @lc app=leetcode id=700 lang=python3
#
# [700] Search in a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root or val == root.val: return root
        if val > root.val:
            return self.searchBST(root.right, val)
        if val < root.val:
            return self.searchBST(root.left, val)

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root and val != root.val:
            if val > root.val:
                root = root.right
            elif val < root.val:
                root = root.left
        return root

# @lc code=end

