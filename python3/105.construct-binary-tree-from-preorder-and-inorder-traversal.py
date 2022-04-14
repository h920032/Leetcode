#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not len(preorder): return None
        root = TreeNode(val = preorder[0])
        if len(preorder) > 1:
            i, j = 0, 1
            while inorder[i] != root.val: i += 1
            root.left = self.buildTree(preorder[1:i + 1], inorder[0:i])
            root.right = self.buildTree(preorder[i + 1:], inorder[i + 1:])
        return root

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_d = {}
        for i in range(len(inorder)):
            inorder_d[inorder[i]] = i
        def build(pre_left, pre_right, in_left, in_right):
            if pre_left == pre_right: return None
            root = TreeNode(val = preorder[pre_left])
            if pre_right - pre_left > 1:
                i = inorder_d[root.val]
                root.left = build(pre_left + 1, pre_left + i - in_left + 1, in_left, i)
                root.right = build(pre_left + i - in_left + 1, pre_right, i + 1, in_right)
            return root
        return build(0, len(preorder), 0, len(inorder))\

# @lc code=end

