#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return head
        if head.next is None: return head
        temp = head.val
        head.val = head.next.val
        head.next.val = temp
        self.swapPairs(head.next.next)
        return head
# @lc code=end

