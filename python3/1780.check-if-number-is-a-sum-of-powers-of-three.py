#
# @lc app=leetcode id=1780 lang=python3
#
# [1780] Check if Number is a Sum of Powers of Three
#

# @lc code=start
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        if n == 0: return True
        if n % 3 == 2: return False
        if n % 3 == 1: return self.checkPowersOfThree(n - 1)
        if n % 3 == 0: return self.checkPowersOfThree(n // 3)
                
# @lc code=end

