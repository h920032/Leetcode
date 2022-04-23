#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#

# @lc code=start
# greedy on start points
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[0])
        min_end = intervals[0][1]
        count = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < min_end:
                min_end = min(min_end, intervals[i][1])
                count += 1
            else:
                min_end = intervals[i][1]
        return count

# greedy on end points
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[1])
        min_end = intervals[0][1]
        count = 1
        for i in range(1, len(intervals)):
            if intervals[i][0] >= min_end:
                min_end = intervals[i][1]
                count += 1
        return len(intervals) - count

# @lc code=end

