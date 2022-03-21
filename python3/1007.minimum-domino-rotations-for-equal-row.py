#
# @lc app=leetcode id=1007 lang=python3
#
# [1007] Minimum Domino Rotations For Equal Row
#

# @lc code=start
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        l = len(tops)
        count = [0] * 6
        for i in range(l):
            if tops[i] != bottoms[i]:
                count[tops[i] - 1] += 1
                count[bottoms[i] - 1] += 1
            else:
                count[tops[i] - 1] += 1
        target = 0
        for i in range(6):
            if count[i] == l:
                target = i + 1
        if not target: return -1
        count_up = 0
        count_down = 0
        for i in range(l):
            if tops[i] != target:
                count_up += 1
            if bottoms[i] != target:
                count_down += 1
        return min(count_up, count_down)
                
# @lc code=end

