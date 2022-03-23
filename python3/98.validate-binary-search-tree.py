#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def val_tree(node):
            if node.left != None and node.right == None:
                left_min, left_max = val_tree(node.left)
                if left_max != None and left_max < node.val:
                    return (left_min, node.val)
            elif node.right != None and node.left == None:
                right_min, right_max = val_tree(node.right)
                if right_min != None and right_min > node.val:
                    return (node.val, right_max)
            elif node.right == None and node.left == None:
                return (node.val, node.val)
            else:
                left_min, left_max = val_tree(node.left)
                right_min, right_max = val_tree(node.right)
                if right_min != None and right_min > node.val and left_max != None and left_max < node.val:
                    return (left_min, right_max)
            return (None, None)
        _min, _max = val_tree(root)
        if _min != None and _max != None:
            return True
        return False
                
# @lc code=end

