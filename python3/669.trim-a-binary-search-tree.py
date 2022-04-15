#
# @lc app=leetcode id=669 lang=python3
#
# [669] Trim a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# simple version
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root: return None
        elif root.val > high: return self.trimBST(root.left, low, high)
        elif root.val < low: return self.trimBST(root.right, low, high)
        else: root.left, root.right = self.trimBST(root.left, low, high), self.trimBST(root.right, low, high)
        return root

class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root: return None
        if root.val == low: 
            root.left = None
            root.right = self.trimBST(root.right, low, high)
            return root
        if root.val == high:
            root.right = None
            root.left = self.trimBST(root.left, low, high)
            return root
        if root.val > low and root.val > high:
            return self.trimBST(root.left, low, high)
        if root.val < low and root.val < high:
            return self.trimBST(root.right, low, high)
        if root.val > low and root.val < high:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
            return root
        
# @lc code=end

