#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#

# @lc code=start
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        d = {}
        word_l = len(words[0])
        target_l = word_l * len(words)
        for w in words:
            if w in d: d[w] += 1
            else: d[w] = 1
        def find(n):
            new_d = d.copy()
            for i in range(n, n + target_l + 1 - word_l, word_l):
                t = s[i:i + word_l]
                if t in new_d and new_d[t]:
                    new_d[t] -= 1
                else: return False
            return True
        out = []
        i = 0
        while i < len(s) - target_l + 1:
            if find(i):
                out.append(i)
            i += 1
        return out
                
# @lc code=end

