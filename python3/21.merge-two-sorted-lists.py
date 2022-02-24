#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        if list1.val <= list2.val:
            return ListNode(val = list1.val, next = self.mergeTwoLists(list1.next, list2))
        else: return ListNode(val = list2.val, next = self.mergeTwoLists(list1, list2.next))
# @lc code=end

