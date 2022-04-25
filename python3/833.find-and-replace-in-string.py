#
# @lc app=leetcode id=833 lang=python3
#
# [833] Find And Replace in String
#

# @lc code=start
class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        data = []
        for i in range(len(indices)):
            data.append([indices[i], sources[i], targets[i]])
        data = sorted(data, key = lambda x:x[0], reverse=True)
        
        for d in data:
            start = d[0]
            match = True
            for j in range(len(d[1])):
                if start + j >= len(s) or d[1][j] != s[start + j]:
                    match = False
                    break
            if match:
                s = s[:start] + d[2] + s[start+len(d[1]):]
        return s
                    
# @lc code=end

