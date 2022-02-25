#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = set()
        s = 0
        s_unique = 0
        for i in nums:
            s += i
            if i not in a:
                a.add(i)
                s_unique += i
        return s_unique * 2 - s
        
            
        
# @lc code=end

