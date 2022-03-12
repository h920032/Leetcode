#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ori = []
        new = []
        new_head=Node(-1)
        ptr = head
        new_ptr = new_head
        while ptr != None:
            ori.append(ptr)
            new_head.next = Node(ptr.val, None, None)
            new.append(new_head.next)
            new_head = new_head.next
            ptr = ptr.next
        for i in range(len(ori)):
            if ori[i].random==None:
                new[i].ramdom=None
            else:
                new[i].random=new[ori.index(ori[i].random)]
        return new_ptr.next
                        
# @lc code=end

