#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        i = -1
        while (i+1)**2 <= x:
            i+=1
        return i
        
# @lc code=end

