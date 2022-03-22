#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        reverse_list = []
        def triverse(node, current, reverse_list):
            if left > current:
                triverse(node.next, current + 1, reverse_list)
            elif right >= current:
                reverse_list.append(node.val)
                triverse(node.next, current + 1, reverse_list)
                node.val = reverse_list[right - current]
            return None
        triverse(head, 1, reverse_list)
        return head
                
# @lc code=end

