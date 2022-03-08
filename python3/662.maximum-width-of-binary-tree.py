#
# @lc app=leetcode id=662 lang=python3
#
# [662] Maximum Width of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def triverse(node_list):
            new_list = []
            max_left = float('inf')
            max_right = 0
            for i,n in node_list:
                if n.left != None:
                    new_list.append((2*i, n.left))
                    max_left = min(max_left, 2*i)
                    max_right = max(max_right, 2*i)
                if n.right != None:
                    new_list.append((2*i + 1, n.right))
                    max_left = min(max_left, 2*i + 1)
                    max_right = max(max_right, 2*i + 1)
            if len(new_list) == 0:
                return 1
            return max(abs(max_right-max_left + 1), triverse(new_list))
        return triverse([(0, root)])
        
# @lc code=end

