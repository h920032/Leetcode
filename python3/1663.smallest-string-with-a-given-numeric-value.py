#
# @lc app=leetcode id=1663 lang=python3
#
# [1663] Smallest String With A Given Numeric Value
#

# @lc code=start
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        k = k - n
        out = ""
        n_z = k // 25
        n_a = n - n_z - (1 * (k % 25 != 0))
        out = n_a * "a" + chr(97 + k % 25) * (k % 25 != 0) + n_z * "z" 
        return out

# too slow
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        k = k - n
        out = ["a"] * n
        for i in range(n - 1, -1, -1):
            out[i] = chr(ord(out[i]) + min(k, 25))
            k -= min(k, 25)
        return "".join(out)
        
# @lc code=end

