#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        start = image[sr][sc]
        if newColor == start: return image
        image[sr][sc] = newColor
        def flood(sr, sc):
            if sr - 1 >= 0 and image[sr- 1][sc] == start:
                image[sr- 1][sc] = newColor
                flood(sr-1, sc)
            if sr + 1 < m and image[sr+ 1][sc] == start:
                image[sr+1][sc] = newColor
                flood(sr+1, sc)
            if sc - 1 >= 0 and image[sr][sc - 1] == start:
                image[sr][sc- 1] = newColor
                flood(sr, sc - 1) 
            if sc + 1 < n and image[sr][sc + 1] == start:
                image[sr][sc+ 1] = newColor
                flood(sr, sc + 1)
        flood(sr,sc)
        return image        
# @lc code=end

