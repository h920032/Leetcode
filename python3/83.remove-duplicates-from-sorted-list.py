#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode(-999, head)
        prev_node = new_head
        after_node = new_head.next
        dup_val = -999
        while after_node != None:
            if after_node.next != None and after_node.val == after_node.next.val:
                if dup_val == after_node.val:
                    after_node = after_node.next
                else:
                    dup_val = after_node.val
                    after_node = after_node.next
            else:
                if dup_val != -999:
                    prev_node.next = after_node.next
                    after_node = after_node.next
                    dup_val = -999
                else:
                    prev_node = prev_node.next
                    after_node = after_node.next
        return new_head.next
                
# @lc code=end

