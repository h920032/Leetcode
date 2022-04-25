#
# @lc app=leetcode id=792 lang=python3
#
# [792] Number of Matching Subsequences
#

# @lc code=start
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        arr = [[] for _ in range(26)]
        count = 0
        for w in words:
            arr[ord(w[0]) - ord('a')].append((w[1:], w))
        
        for c in s:
            temp = arr[ord(c) - ord('a')].copy()
            arr[ord(c) - ord('a')] = []
            for w in temp:
                if len(w[0]) == 0: count += 1
                else: arr[ord(w[0][0]) - ord('a')].append((w[0][1:], w[0]))
        return count
                
# @lc code=end

