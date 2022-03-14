#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def triverse(i, c):
            if i == 1: return [[c]]
            out = []
            for j in nums:
                if c == j:
                    continue
                for s in triverse(i - 1, j):
                    if c not in s:
                        out.append([c] + s)
            return out
        return [j for i in nums for j in triverse(len(nums), i)]
        
# @lc code=end

