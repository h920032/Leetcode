#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr_s = [0] * 26
        arr_t = [0] * 26
        for c in s:
            arr_s[ord(c) - ord('a')] += 1
        for c in t:
            arr_t[ord(c) - ord('a')] += 1
        return hash(tuple(arr_s)) == hash(tuple(arr_t))
                
# @lc code=end

