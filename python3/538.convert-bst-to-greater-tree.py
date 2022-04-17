#
# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traverse(root, s):
            if not root: return s
            root.val += traverse(root.right, s)
            return traverse(root.left, root.val)
        traverse(root, 0)
        return root
                
# @lc code=end

