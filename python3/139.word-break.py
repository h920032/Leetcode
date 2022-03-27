#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        d = set()
        for w in wordDict:
            d.add(w)
        @cache
        def dp(n):
            if n == len(s): return True
            out = False
            for i in range(n, len(s)):
                print(s[n:i + 1])
                if s[n:i + 1] in d:
                    out = dp(i + 1) or out
            return out
        return dp(0)

# bottom up dp
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        d = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if s[j:i] in d and dp[j]:
                    dp[i] = True
                    break
        return dp[len(s)]

# @lc code=end

