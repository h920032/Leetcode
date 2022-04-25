#
# @lc app=leetcode id=2013 lang=python3
#
# [2013] Detect Squares
#

# @lc code=start
class DetectSquares:
    def __init__(self):
        self.d = {}

    def add(self, point: List[int]) -> None:
        if (point[0], point[1]) in self.d: self.d[(point[0], point[1])] += 1
        else: self.d[(point[0], point[1])] = 1

    def count(self, point: List[int]) -> int:
        x1, y1 = point[0], point[1]
        count = 0
        for n in self.d:
            x2, y2 = n
            x_diff = -(x1-x2)
            y_diff = y1-y2
            if (x_diff == 0 or y_diff == 0) and x_diff != y_diff:
                if (x1 + y_diff,y1 + x_diff) in self.d and (x2 + y_diff,y2 + x_diff) in self.d:
                    count += self.d[(x1 + y_diff,y1 + x_diff)] * self.d[(x2 + y_diff,y2 + x_diff)] * self.d[n]
        return count
                
# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)       


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
# @lc code=end

