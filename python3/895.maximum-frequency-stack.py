#
# @lc app=leetcode id=895 lang=python3
#
# [895] Maximum Frequency Stack
#

# @lc code=start
class FreqStack:
    def __init__(self):
        self.d = {}
        self.order_list = []

    def push(self, val: int) -> None:
        if val not in self.d:
            self.d[val] = 1
        else:
            self.d[val] += 1
        if len(self.order_list) < self.d[val]:
            self.order_list.append([val])
        else:
            self.order_list[self.d[val] - 1].append(val)

    def pop(self) -> int:
        if len(self.order_list) > 0:
            out = self.order_list[-1].pop()
            self.d[out] -= 1
            if len(self.order_list[-1]) == 0:
                self.order_list.pop()
            return out
        return None        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
# @lc code=end

