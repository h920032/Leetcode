#
# @lc app=leetcode id=218 lang=python3
#
# [218] The Skyline Problem
#

# @lc code=start
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        position = set([b[0] for b in buildings] + [b[1] for b in buildings])
        position = sorted(position)
        
        heap = []
        sky_line = [[-1, 0]]
        
        i = 0
        for p in position:
            while i < len(buildings) and buildings[i][0] <= p:
                heappush(heap, (-buildings[i][2], buildings[i][1]))
                i += 1
            while heap and heap[0][1] <= p:
                heappop(heap)
            h = 0
            if heap: h = -heap[0][0]
            if sky_line[-1][1] != h:
                sky_line.append([p, h])
        return sky_line[1:]
                
# @lc code=end

