#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start
class Solution:
    def add(self, num1: str, num2: str):
        l1 = len(num1)
        l2 = len(num2)
        if l2 > l1:
            return self.add(num2, num1)
        p = 0
        out = ""
        for i in range(l1):
            s = 0
            if i < l2:
                s = int(num2[l2 - i - 1]) + int(num1[l1 - i - 1]) + p
            else:
                s = int(num1[l1 - i - 1]) + p
            p = s//10
            out = str(s%10) + out
        if p != 0:
            out = str("1") + out
        return out
        
    def multiply(self, num1: str, num2: str) -> str:
        l1 = len(num1)
        l2 = len(num2)
        if l2 > l1:
            return self.multiply(num2, num1)
        zero = ""
        out = "0"
        for i in range(l2 - 1, -1, -1):
            for j in range(int(num2[i])):
                out = self.add(out, num1 + zero)
            zero += "0"
        return out
                
# @lc code=end

