#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        @cache
        def backtrack(i, j):
            out = []
            if i == j:
                return None
            for num in range(i, j):
                left = backtrack(i, num)
                right = backtrack(num + 1, j)
                if left == None and right == None:
                    out.append(TreeNode(num + 1, None, None))
                elif left == None:
                    for r in right:
                        out.append(TreeNode(num + 1, None, r))
                elif right == None:
                    for l in left:
                        out.append(TreeNode(num + 1, l, None))
                else:
                    for l in left:
                        for r in right:
                            out.append(TreeNode(num + 1, l, r))
            return out
        return backtrack(0, n)   
                    
# @lc code=end

