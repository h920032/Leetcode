#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        c = 0
        for i in lists:
            if i is None:
                c += 1
        for i in range(c):
            lists.remove(None)
        if len(lists) == 0: return None
        def heap_sort(i):
            k = len(lists)
            if 2*i > k: return True
            if 2*i == k:
                if lists[i-1].val > lists[2*i-1].val:
                    temp = lists[i - 1]
                    lists[i - 1] = lists[2*i - 1]
                    lists[2*i - 1] = temp
                return True
            heap_sort(2*i)
            heap_sort(2*i + 1)
            if lists[i-1].val > min(lists[2*i-1].val, lists[2*i].val):
                if lists[2*i-1].val > lists[2*i].val:
                    temp = lists[i - 1]
                    lists[i - 1] = lists[2*i]
                    lists[2*i] = temp
                    heap_sort(2*i + 1)
                else:
                    temp = lists[i - 1]
                    lists[i - 1] = lists[2*i - 1]
                    lists[2*i - 1] = temp
                    heap_sort(2*i)
            return True
        
        def heap_check(i):
            k = len(lists)
            if 2*i > k: return True
            if 2*i == k:
                if lists[i-1].val > lists[2*i-1].val:
                    temp = lists[i - 1]
                    lists[i - 1] = lists[2*i - 1]
                    lists[2*i - 1] = temp
                return True
            if lists[i-1].val > min(lists[2*i-1].val, lists[2*i].val):
                if lists[2*i-1].val > lists[2*i].val:
                    temp = lists[i - 1]
                    lists[i - 1] = lists[2*i]
                    lists[2*i] = temp
                    heap_check(2*i + 1)
                else:
                    temp = lists[i - 1]
                    lists[i - 1] = lists[2*i - 1]
                    lists[2*i - 1] = temp
                    heap_check(2*i)
            return True
            
        
        def heap_pop():
            temp = lists[0]
            lists[0] = lists[0].next
            temp.next = None
            if lists[0] == None:
                temp2 = lists[-1]
                lists[-1] = lists[0]
                lists[0] = temp2
                lists.pop()
            heap_check(1)
            return temp
        
        heap_sort(1)
        result = heap_pop()
        head = result
        while len(lists) > 0:
            head.next = heap_pop()
            head = head.next
        return result

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        if list1.val <= list2.val:
            return ListNode(val = list1.val, next = self.mergeTwoLists(list1.next, list2))
        else: return ListNode(val = list2.val, next = self.mergeTwoLists(list1, list2.next))

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        if k == 0: return None
        if k == 1: return lists[0]
        if k == 2: return self.mergeTwoLists(lists[0], lists[1])
        return self.mergeTwoLists(self.mergeKLists(lists[:k//2]),self.mergeKLists(lists[k//2:]))


        
            

# @lc code=end

