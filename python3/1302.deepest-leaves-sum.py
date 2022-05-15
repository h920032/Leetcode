#
# @lc app=leetcode id=1302 lang=python3
#
# [1302] Deepest Leaves Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if root.left == None and root.right == None: return 0, root.val
            if root.left == None:
                d,s = dfs(root.right)
                return d + 1, s
            if root.right == None:
                d,s = dfs(root.left)
                return d + 1, s
            d_l,s_l = dfs(root.left)
            d_r,s_r = dfs(root.right)
            if d_l > d_r:
                return d_l + 1, s_l
            if d_r > d_l:
                return d_r + 1, s_r
            return d_l + 1, s_l + s_r
        return dfs(root)[1]
                
# @lc code=end

