#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        add = 0
        out = ListNode()
        Next = out
        while l1 != None or l2 != None:
            if l1 != None and l2 != None:
                s = l1.val + l2.val + add
                l1 = l1.next
                l2 = l2.next
            elif l1 != None:
                s = l1.val + add
                l1 = l1.next
            elif l2 != None:
                s = l2.val + add
                l2 = l2.next
            if s >= 10:
                add = 1
                Next.val = s-10
            else:
                add = 0
                Next.val = s
            if l1 != None or l2 != None:
                Next.next = ListNode()
                Next = Next.next
        if add == 1:
            Next.next = ListNode()
            Next = Next.next
            Next.val = 1
        return out
# @lc code=end

