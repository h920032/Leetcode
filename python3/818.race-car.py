#
# @lc app=leetcode id=818 lang=python3
#
# [818] Race Car
#

# @lc code=start
class Solution:
    def racecar(self, target: int) -> int:
        visited = {}
        def dp(i):
            if i in visited: return visited[i]
            n = i.bit_length()
            if (i + 1) & i == 0: 
                visited[i] =  n
                return visited[i]
            visited[i] = dp(2**n - 1 - i) + n + 1
            for m in range(n - 1):
                visited[i] = min(visited[i], dp(i - 2**(n - 1) +  2**m) + n + m + 1)
            return visited[i]
        return dp(target)
        
# @lc code=end

