#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        s_r = s[::-1]
        l = len(s)
        count = 0
        for i in range(l + 1):
            for j in range(i + 1, l + 1):
                if s[i:j] == s_r[l - j:l - i]: count += 1
        return count

# manacher algo
class Solution:
    def countSubstrings(self, S):
        S = '#' + '#'.join(S) + '#'
        p = [0] * len(S)
        max_right = 0
        max_center = 0
        for i in range(1, len(S) - 1):
            if i <= max_right:
                p[i] = min(p[max_center * 2 - i], p[max_right - i])
            while i - p[i] - 1 >= 0 and i + p[i] + 1 < len(S) and S[i + p[i] + 1] == S[i - p[i] - 1]:
                p[i] += 1
            if i + p[i] > max_right:
                max_center = i
                max_right = max_center + p[i]
        result = 0
        for i in range(len(p)):
            result += (p[i] + 1) // 2
        return result
            
            


# @lc code=end

