#
# @lc app=leetcode id=539 lang=python3
#
# [539] Minimum Time Difference
#

# @lc code=start
# bucket sort
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        time = [0] * (24*60)
        for t in timePoints:
            if time[int(t[:2]) * 60 + int(t[3:])] != 0: return 0
            time[int(t[:2]) * 60 + int(t[3:])] += 1
        min_diff = float('inf')
        first = -1
        count = 1
        for i in range(24*60):
            if first == -1 and time[i] != 0:
                first = i
            elif time[i] != 0:
                min_diff = min(count, min_diff)
                count = 1
            elif first != -1: count += 1
        min_diff = min(count + first, min_diff)
        return min_diff
                
# @lc code=end

