#
# @lc app=leetcode id=1721 lang=python3
#
# [1721] Swapping Nodes in a Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        target = [None, None]
        def findNode(node, r):
            if not node: return k
            if r == 1: target[0] = node
            n = findNode(node.next, r - 1)
            if n == 1: target[1] = node
            return n - 1
        findNode(head, k)
        target[0].val, target[1].val = target[1].val, target[0].val
        return head
                
# @lc code=end

