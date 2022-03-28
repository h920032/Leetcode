#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = [-float(inf)]
        def dfs(node):
            if not node: return 0
            l_max, r_max = max(dfs(node.left), 0), max(dfs(node.right), 0)
            max_path[0] = max(max_path[0], l_max + r_max + node.val)
            return node.val + max(l_max, r_max)
        dfs(root)
        return max_path[0]
                
# @lc code=end

