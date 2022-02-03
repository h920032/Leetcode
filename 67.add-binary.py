#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        la = len(a)
        lb = len(b)
        out = ""
        add = 0
        while la > 0 or lb > 0:
            if lb <= 0:
                s = int(a[la-1]) + add
            elif la <= 0:
                s = int(b[lb-1]) + add
            else:
                s = int(a[la-1]) + int(b[lb-1]) + add
            if s >= 2:
                add = 1
                out = str(s - 2) + out
            else:
                out = str(s) + out
                add = 0
            la -= 1
            lb -= 1
        if add == 1: return '1' + out
        else: return out

# @lc code=end

