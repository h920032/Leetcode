#
# @lc app=leetcode id=1379 lang=python3
#
# [1379] Find a Corresponding Node of a Binary Tree in a Clone of That Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(org, clon):
            if not org: return None
            if org == target: return clon
            l = dfs(org.left, clon.left)
            if l: return l
            r = dfs(org.right, clon.right)
            if r: return r
            return None
        return dfs(original, cloned)
                
# @lc code=end

