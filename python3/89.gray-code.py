#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#

# @lc code=start
class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 1: return [0, 1]
        pre = self.grayCode(n - 1)
        return pre + [2**(n - 1) + pre[i] for i in range(len(pre) - 1, -1, -1)]
                
# @lc code=end

