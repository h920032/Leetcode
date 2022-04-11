#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        s = list(itertools.accumulate(height))
        l, r = 0, len(height) - 1
        prev_l, prev_r = -1, -1
        max_h = 0
        w = 0
        while l < r:
            if height[l] > max_h and height[r] > max_h:
                if prev_l != -1:
                    if prev_l + 1 < l:
                        w += max_h * (l - prev_l - 1) - (s[l - 1] - s[prev_l])
                    if r + 1 < prev_r:
                        w += max_h * (prev_r - r - 1) - (s[prev_r - 1] - s[r])
                prev_l, prev_r = l, r
                max_h = min(height[l], height[r])
            elif height[l] > max_h:
                r -= 1
            else:
                l += 1
        if prev_l != -1:
            if prev_l + 1 < l:
                w += max_h * (l - prev_l - 1) - (s[l - 1] - s[prev_l])
            if r + 1 < prev_r:
                w += max_h * (prev_r - r - 1) - (s[prev_r - 1] - s[r])
        return w

# Dynamic Programming
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        w, max_l, max_r = 0, 0, 0
        while l < r:
            if height[l] < height[r]:
                if height[l] >= max_l: max_l = height[l]
                else: w += max_l - height[l]
                l += 1
            else:
                if height[r] >= max_r: max_r = height[r]
                else: w += max_r - height[r]
                r -= 1
        return w

# @lc code=end

