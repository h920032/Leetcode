#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left = 0
        right = len(intervals)
        left_end = -1
        right_end = -1
        if right == 0:
            return [newInterval]
        if intervals[0][0] > newInterval[1]: return [newInterval] + intervals
        if intervals[-1][1] < newInterval[0]: return intervals + [newInterval]
        while left < right:
            mid = left + (right - left) // 2
            if intervals[mid][0] > newInterval[0]:
                right = mid
            elif intervals[mid][1] < newInterval[0]:
                left = mid + 1
            else: 
                left_end = mid
                break
        if left_end == -1: left_end = right
        
        left = 0
        right = len(intervals)
        while left < right:
            mid = left + (right - left) // 2
            if intervals[mid][0] > newInterval[1]:
                right = mid
            elif intervals[mid][1] < newInterval[1]:
                left = mid + 1
            else: 
                right_end = mid
                break
        if right_end == -1: right_end = right - 1
        print(right_end)
        return intervals[:left_end] + [[min(intervals[left_end][0], newInterval[0]), max(intervals[right_end][1], newInterval[1])]] + intervals[right_end + 1:]   
             
# @lc code=end

