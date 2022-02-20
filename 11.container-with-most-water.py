#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = len(height)
        def dp(n):
            if n == 0: return 0
            if n == 1: return (0, 1, min(height[0], height[1]))
            left, right, max_area = dp(n - 1)
            a = min(height[left], height[n]) * (n - left)
            b = min(height[right], height[n]) * (n - right)
            if a > b and a >= max_area:
                return (left, n, a)
            if b > a and b >= max_area:
                return (right, n, b)
            return (left, right, max_area)
        return dp(len)
'''

class Solution:
    def maxArea(self, height) -> int:
        l = len(height)
        left = 0
        right = l - 1
        @cache
        def dp(l, r):
            area = min(height[l], height[r]) * (r - l)
            if height[l] > height[r]:
                org = height[r]
                while l < r:
                    r -= 1
                    if height[r] > org: 
                        return max(area, dp(l, r))
            else:
                org = height[l]
                while l < r:
                    l += 1
                    if height[l] > org: 
                        return max(area, dp(l, r))
            return area
        return dp(left, right)




# @lc code=end

