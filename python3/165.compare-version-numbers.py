#
# @lc app=leetcode id=165 lang=python3
#
# [165] Compare Version Numbers
#

# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v_1 = version1.split('.')
        v_2 = version2.split('.')
        l1 = len(v_1)
        l2 = len(v_2)
        one_sum = 0
        two_sum = 0
        for i in range(max(l1,l2)):
            one_sum *= 10
            two_sum *= 10
            if i + 1 > l1 and i + 1 <= l2:
                two_sum += int(v_2[i])
            elif i + 1 > l2 and i + 1 <= l1:
                one_sum += int(v_1[i])
            else:
                one_sum += int(v_1[i])
                two_sum += int(v_2[i])
        if one_sum>two_sum: return 1
        if one_sum<two_sum: return -1
        if one_sum==two_sum: return 0
# @lc code=end

