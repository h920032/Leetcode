#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Recursive
class Solution:
    def traverse(self, node, next_node, k):
        if not next_node: return None, None
        if k == 0:
            post_node = next_node.next
            next_node.next = node
            return next_node, post_node
        new_head, post_node = self.traverse(next_node, next_node.next, k - 1)
        if new_head:
            next_node.next = node
        return new_head, post_node
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head
        new_head, post_node = self.traverse(head, head.next, k - 2)
        if new_head:
            head.next = self.reverseKGroup(post_node, k)
            return new_head
        return head

# iterative
class Solution:
    def reverseList(self, head, k):
        pre_node = None
        post_node = head.next
        count = 1
        while count < k:
            head.next = pre_node
            pre_node = head
            head = post_node
            post_node = post_node.next
            count += 1
        head.next = pre_node
        return head
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ptr = head
        tail = None
        new_head = None
        while ptr:
            count = 0
            while count < k and ptr:
                count += 1
                ptr = ptr.next
            if count == k:
                if not tail:
                    new_head = self.reverseList(head, k)
                else:
                    tail.next = self.reverseList(head, k)
                tail = head
                head = ptr
        tail.next = head
        return new_head

# @lc code=end

