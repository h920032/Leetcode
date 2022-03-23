#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        node_list = []
        def inOrder(node):
            if node.left != None:
                inOrder(node.left)   
            node_list.append(node)
            if node.right != None:
                inOrder(node.right)
        inOrder(root)
        left = 0
        right = len(node_list) - 1
        for i in range(len(node_list) - 1):
            if node_list[i].val > node_list[i + 1].val:
                left = i
                break
        for i in range(len(node_list) - 1, 0, -1):
            if node_list[i - 1].val > node_list[i].val:
                right = i
                break
        temp = node_list[left].val
        node_list[left].val = node_list[right].val 
        node_list[right].val = temp

#O(1) space
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        node_list = [None, None, None]
        def inOrder(node):
            if node.left != None:
                inOrder(node.left)   
            if node_list[0] == None:
                node_list[0] = node
            elif node_list[1] == None and node_list[0].val > node.val:
                node_list[1] = node_list[0]
                if node_list[0].val > node.val:
                    node_list[2] = node
            elif node_list[0].val > node.val:
                node_list[2] = node
            else:
                node_list[0] = node
            if node.right != None:
                inOrder(node.right)
        inOrder(root)
        temp = node_list[1].val
        node_list[1].val = node_list[2].val 
        node_list[2].val = temp

# @lc code=end

