#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        l = len(s)
        @cache
        def backtrack(n, r):
            out = []
            if r == 0:
                if n == l: return [[]]
                else: return None
            for i in range(3):
                if i > 0 and n + i + 1 <= l and s[n] == '0': break
                if n + i + 1 <= l and int(s[n:n+i+1]) <= 255:
                    if backtrack(n + i + 1, r - 1) != None:
                        out += [[s[n:n+i+1]] + t for t in backtrack(n + i + 1, r - 1)]
            return out
        return [".".join(i) for i in backtrack(0, 4)]
                
# @lc code=end

