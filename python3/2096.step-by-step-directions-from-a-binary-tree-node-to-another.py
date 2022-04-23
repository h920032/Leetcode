#
# @lc app=leetcode id=2096 lang=python3
#
# [2096] Step-By-Step Directions From a Binary Tree Node to Another
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        startPath = []
        destPath = []
        def traverse_start(root, val, path_list):
            if not root: return False
            if root.val == val: return True
            if traverse_start(root.left, val, path_list):
                path_list.append('L')
                return True
            if traverse_start(root.right, val, path_list):
                path_list.append('R')
                return True
            return False
        
        def traverse_dest(root, val, path_list, dest_list):
            if not root: return False
            if root.val == val: return True
            if len(dest_list) == 0 and len(path_list) > 0 and path_list[-1] == 'L':
                path_list.pop()
                if traverse_dest(root.left, val, path_list, dest_list): return True
                path_list.append('L')
            else:
                dest_list.append('L')
                if traverse_dest(root.left, val, path_list, dest_list): return True
                dest_list.pop()
            if len(dest_list) == 0 and len(path_list) > 0 and path_list[-1] == 'R':
                path_list.pop()
                if traverse_dest(root.right, val, path_list, dest_list): return True
                path_list.append('R')
            else:
                dest_list.append('R')
                if traverse_dest(root.right, val, path_list, dest_list): return True
                dest_list.pop()
        
        traverse_start(root, startValue, startPath)
        traverse_dest(root, destValue, startPath, destPath)
        return 'U' * len(startPath) + ''.join(destPath)
                
# @lc code=end

