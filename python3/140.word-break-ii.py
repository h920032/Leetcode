#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        d = set(wordDict)
        @cache
        def dp(n):
            if n == len(s): return [[]]
            out = []
            for i in range(n, len(s)):
                if s[n:i + 1] in d:
                    r = dp(i + 1)
                    if r:
                        for l in r:
                            out.append([s[n:i + 1]] + l)
            return out
        return [" ".join(l) for l in dp(0)]

# with less memory
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        d = {}
        for i, c in enumerate(wordDict):
            d[c] = i
        @cache
        def dp(n):
            if n == len(s): return [[]]
            out = []
            for i in range(n, len(s)):
                if s[n:i + 1] in d:
                    r = dp(i + 1)
                    if r:
                        for l in r:
                            out.append([d[s[n:i + 1]]] + l)
            return out
        return [" ".join([wordDict[k] for k in l]) for l in dp(0)]

# @lc code=end

