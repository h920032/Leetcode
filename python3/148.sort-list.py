#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def bubbleSwap(head):
            if head is None or head.next is None: return True
            if head.next.val < head.val:
                temp = head.val
                head.val = head.next.val
                head.next.val = temp
                return False and bubbleSwap(head.next)
            return bubbleSwap(head.next)
        while not bubbleSwap(head):
            pass
        return head

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def mergeTwoLists(list1, list2):
            if list1 == None:
                return list2
            elif list2 == None:
                return list1
            if list1.val <= list2.val:
                return ListNode(val = list1.val, next = mergeTwoLists(list1.next, list2))
            else: return ListNode(val = list2.val, next = mergeTwoLists(list1, list2.next))
        
        def mergeSort(head):
            temp = head
            c = 0
            while temp is not None:
                c += 1
                temp = temp.next
            if c <= 1:
                return head
            if c == 2:
                if head.val > head.next.val:
                    t = head.val
                    head.val = head.next.val
                    head.next.val = t
                    return head
                else:
                    return head
            temp = head
            for i in range(c//2):
                temp = temp.next
            left = head
            right = temp.next
            temp.next = None
            left = mergeSort(left)
            right = mergeSort(right)
            return mergeTwoLists(left, right)  
        
        return mergeSort(head)

# @lc code=end

