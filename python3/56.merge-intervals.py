#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def merge_sort(intervals_list):
            l = len(intervals_list)
            if l == 1: return intervals_list
            if l == 2:
                if intervals_list[0][1] < intervals_list[1][0]:
                    return intervals_list
                if intervals_list[0][0] > intervals_list[1][1]:
                    return [intervals_list[1], intervals_list[0]]
                return [[min(intervals_list[0][0], intervals_list[1][0]), max(intervals_list[0][1], intervals_list[1][1])]]
            out = []
            a = merge_sort(intervals_list[:l//2])
            b = merge_sort(intervals_list[l//2:])
            i_a = 0
            i_b = 0
            while i_a < len(a) and i_b < len(b):
                if a[i_a][1] < b[i_b][0]:
                    if len(out) > 0 and out[-1][1] >= a[i_a][0]:
                        out[-1][1] = max(out[-1][1], a[i_a][1])
                    else:
                        out.append(a[i_a])
                    i_a += 1
                    continue
                if a[i_a][0] > b[i_b][1]:
                    if len(out) > 0 and out[-1][1] >= b[i_b][0]:
                        out[-1][1] = max(out[-1][1], b[i_b][1])
                    else:
                        out.append(b[i_b])
                    i_b += 1
                    continue
                if len(out) > 0 and out[-1][1] >= min(a[i_a][0], b[i_b][0]):
                        out[-1][1] = max(out[-1][1], max(a[i_a][1], b[i_b][1]))
                else:
                    out.append([min(a[i_a][0], b[i_b][0]), max(a[i_a][1], b[i_b][1])])
                i_a += 1
                i_b += 1
            if i_a < len(a):
                for i in range(i_a, len(a)):
                    if len(out) > 0 and out[-1][1] >= a[i][0]:
                        out[-1][1] = max(out[-1][1], a[i][1])
                    else:
                        out.append(a[i])
            if i_b < len(b):
                for i in range(i_b, len(b)):
                    if len(out) > 0 and out[-1][1] >= b[i][0]:
                        out[-1][1] = max(out[-1][1], b[i][1])
                    else:
                        out.append(b[i])
            return out
        return merge_sort(intervals)        
# @lc code=end

