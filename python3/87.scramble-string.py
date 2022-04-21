#
# @lc app=leetcode id=87 lang=python3
#
# [87] Scramble String
#

# @lc code=start
class Solution:
    @cache
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2: return True
        if len(s1) <= 1: return False
        s1_hash_l = [0] * 26
        s2_hash_l = [0] * 26
        s2_hash_r = [0] * 26
        result = False
        for i in range(len(s1) - 1):
            s1_hash_l[ord(s1[i]) - ord('a')] += 1
            s2_hash_l[ord(s2[i]) - ord('a')] += 1
            s2_hash_r[ord(s2[len(s2)-i-1]) - ord('a')] += 1
            if s1_hash_l == s2_hash_l:
                result = result or (self.isScramble(s1[:i+1], s2[:i+1]) and self.isScramble(s1[i+1:], s2[i+1:]))
            if s1_hash_l == s2_hash_r:
                result = result or (self.isScramble(s1[:i+1], s2[len(s2)-i-1:]) and self.isScramble(s1[i+1:], s2[:len(s2)-i-1]))
        return result
                
# @lc code=end

