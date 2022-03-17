#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#

# @lc code=start
# Definition for singly-linked list.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        low_head = ListNode()
        low_ptr = low_head
        high_head = ListNode()
        high_ptr = high_head
        ptr = head
        while ptr!=None:
            if ptr.val < x:
                low_ptr.next = ptr
                low_ptr = low_ptr.next
                ptr = ptr.next
                low_ptr.next = None
            else:
                high_ptr.next = ptr
                high_ptr = high_ptr.next
                ptr = ptr.next
                high_ptr.next = None
        low_ptr.next = high_head.next
        return low_head.next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        low_ptr = low_head = ListNode()
        high_ptr = high_head = ListNode()
        while head:
            if head.val < x:
                low_ptr.next = head
                low_ptr = low_ptr.next
            else:
                high_ptr.next = head
                high_ptr = high_ptr.next
            head = head.next
        high_ptr.next = None
        low_ptr.next = high_head.next
        return low_head.next


# @lc code=end

