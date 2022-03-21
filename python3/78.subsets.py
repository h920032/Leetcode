#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        def triverse(m):
            out = []
            if m == l: return [[]]
            for i in triverse(m + 1):
                out.append(i)
                out.append([nums[m]] + i)
            return out
        return triverse(0)
                
# @lc code=end

