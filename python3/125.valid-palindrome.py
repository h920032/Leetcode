#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for c in s.lower():
            if c.isnumeric() or c.isalpha():
                new_s += c
        l, r = 0, len(new_s) - 1
        while l < r:
            if new_s[l] == new_s[r]:
                l += 1
                r -= 1
            else: return False
        return True

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l, r = 0, len(s) - 1
        while l < r:
            if not (s[l].isnumeric() or s[l].isalpha()): l += 1
            if not (s[r].isnumeric() or s[r].isalpha()): r -= 1
            if (s[l].isnumeric() or s[l].isalpha()) and (s[r].isnumeric() or s[r].isalpha()):
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else: return False
        return True

# @lc code=end

