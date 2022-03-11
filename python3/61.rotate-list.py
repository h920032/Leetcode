#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None: return head
        new_head = ListNode(0, head)
        def triverse(node, count):
            if node.next != None:
                count = triverse(node.next, count + 1) - 1
                if count == 0:
                    new_head.next = node.next
                    node.next = None
                    return 0
                return count
            else:
                if k % count != 0: node.next = head
                return k % count
        triverse(head, 1)
        return new_head.next    
    
# @lc code=end

