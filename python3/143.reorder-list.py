#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        a = []
        ptr = head.next
        while ptr:
            a.append(ptr)
            ptr = ptr.next
        ptr = head
        tail = True
        while a:
            if tail:
                ptr.next = a[-1]
                a.pop()
            else:
                ptr.next = a[0]
                a = a[1:]
            ptr = ptr.next
            tail = not tail
        ptr.next = None
                
# @lc code=end

