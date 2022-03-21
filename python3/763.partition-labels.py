#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#

# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]][0] = i
                d[s[i]][1] += 1
            else: d[s[i]] = [i, 1]
        max_index = d[s[0]][0]
        count_set = set([s[0]])
        c_sum = d[s[0]][1]
        out = []
        for i in range(len(s)):
            if s[i] not in count_set:
                count_set.add(s[i])
                c_sum += d[s[i]][1]
            if d[s[i]][0] > max_index:
                max_index = d[s[i]][0]
            if i == max_index:
                out.append(c_sum)
                count_set = set()
                c_sum = 0
        return out

# @lc code=end

