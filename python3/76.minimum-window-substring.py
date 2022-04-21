#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        if n > m: return ""
        d = {}
        for c in t:
            if c not in d:d[c] = 1
            else: d[c] += 1
        word_count = 0
        l, r = 0, 0
        min_l, min_r = 0, m
        sub_find = False
        while l <= r:
            if word_count < n and r < m:
                if s[r] in d:
                    if d[s[r]] > 0: word_count += 1
                    d[s[r]] -= 1
                r += 1
            else:
                if l < m and s[l] in d:
                    d[s[l]] += 1
                    if d[s[l]] > 0: word_count -= 1
                l += 1
            if word_count == n:
                if min_r-min_l >= r - l:
                    sub_find = True
                    min_r, min_l = r, l
        if not sub_find: return ''
        return s[min_l:min_r]
                        
# @lc code=end

