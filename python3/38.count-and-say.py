#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return "1"
        s = []
        for i in self.countAndSay(n - 1):
            if len(s) == 0 or s[-1][0] != i:
                s.append([i, 1])
            else:
                s[-1][1] += 1
        r = ""
        for i in s:
            r += str(i[1]) + i[0]
        return r
        

# @lc code=end

