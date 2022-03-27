#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        d = {}
        d[s[0]] = 0
        max_length = 0
        while right < len(s):
            if s[right] not in d: d[s[right]] = 1
            else: d[s[right]] += 1
            if right - left - max(d.values()) < k:
                max_length = max(right - left + 1, max_length)
            else:
                d[s[left]] -= 1
                left += 1
            right += 1
        return max_length
                
# @lc code=end

