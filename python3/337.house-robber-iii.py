#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def dp(i: bool, r: Optional[TreeNode]) -> int:
            if r == None: return 0
            if i: return max(r.val + dp(False, r.left) + dp(False, r.right),
                            dp(True, r.left) + dp(True, r.right))
            else: return dp(True, r.left) + dp(True, r.right)
        return dp(True, root)
        
# @lc code=end

