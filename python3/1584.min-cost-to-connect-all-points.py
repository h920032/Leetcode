#
# @lc app=leetcode id=1584 lang=python3
#
# [1584] Min Cost to Connect All Points
#

# @lc code=start
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def distance(p1, p2):
            return abs(points[p1][0] - points[p2][0]) + abs(points[p1][1] - points[p2][1])
        
        heap = [(0,0)]
        find = set()
        s = 0
        
        while heap:
            w, p = heappop(heap)
            if p in find: continue
            s += w
            find.add(p)
            for i in range(len(points)):
                if i not in find:
                    heappush(heap, (distance(p,i), i))
        return s
                
# @lc code=end

