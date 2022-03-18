#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            if tuple(sorted(i)) not in d:
                d[tuple(sorted(i))] = [i]
            else:
                d[tuple(sorted(i))].append(i)
        return list(d.values())
                    
# @lc code=end

