#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#

# @lc code=start
from queue import Queue

class MyStack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        self.size = 0

    def push(self, x: int) -> None:
        self.q1.put(x)
        self.size += 1

    def pop(self) -> int:
        while self.q1.qsize() != 1:
            self.q2.put(self.q1.get())
        out = self.q1.get()
        self.size -= 1
        self.q1, self.q2 = self.q2, self.q1
        return out

    def top(self) -> int:
        while self.q1.qsize() != 1:
            self.q2.put(self.q1.get())
        out = self.q1.get()
        self.q2.put(out)
        self.q1, self.q2 = self.q2, self.q1
        return out

    def empty(self) -> bool:
        return self.size == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

