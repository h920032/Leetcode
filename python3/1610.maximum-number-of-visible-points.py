#
# @lc app=leetcode id=1610 lang=python3
#
# [1610] Maximum Number of Visible Points
#

# @lc code=start
class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        degree = []
        count = 0
        max_count = 0
        x1, y1 = location[0], location[1]
        for p in points:
            x2, y2 = p[0], p[1]
            x_diff = x2-x1
            y_diff = y2-y1
            if x_diff == 0 and y_diff == 0:
                count += 1
                continue
            if x_diff == 0 and y_diff > 0: degree.append(90)
            elif x_diff == 0 and y_diff < 0: degree.append(270)
            elif x_diff > 0:
                d = atan(y_diff/x_diff) * 180 / pi
                degree.append(d)
            else:
                d = 180+atan(y_diff/x_diff) * 180 / pi
                degree.append(d)
        degree = sorted(degree)
        print(degree)
        for i in range(len(degree)):
            degree.append(degree[i] + 360)
        l, r = 0, 0
        while r < len(degree):
            if degree[l] + angle >= degree[r]:
                r += 1
                count += 1
                max_count = max(count, max_count)
            else: 
                l += 1
                count -= 1
        max_count = max(max_count, count)
        return max_count
                
# @lc code=end

