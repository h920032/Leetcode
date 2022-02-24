#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def rec(head, n):
            a = n
            if head.next is not None:
                a, ptr = rec(head.next, n)
            head.next = ptr
            if a == 1:
                return (a - 1, head.next)
            if a > 1: return (a - 1, head)
            if a == 0: return (0, head)
        return rec(head, n)[1]

# @lc code=end

