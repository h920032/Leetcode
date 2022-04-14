#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        c = 0
        def count(root):
            nonlocal c
            if not root: return -1
            l = count(root.left)
            if l != -1: return l
            c += 1
            if c == k: return root.val
            r = count(root.right)
            if r != -1: return r
            return -1
        return count(root)
                
# @lc code=end

