#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        @cache
        def triverse(i, c):
            if i == 1: return [[c]]
            out = []
            for j in index:
                if c == j:
                    continue
                for s in triverse(i - 1, j):
                    if c not in s:
                        out.append([c] + s)
            return out
        index = list(range(len(nums)))
        out = []
        for i in index:
            for j in triverse(len(nums), i):
                r = [nums[x] for x in j]
                if r not in out:
                    out.append(r)
        return out

# with dict
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        d = {} 
        for i in nums:
            if i in d: d[i] += 1
            else: d[i] = 1
        l = list(d)
        def triverse(r, c):
            out = []
            for i in range(len(r)):
                if r[i] > 0:
                    r_new = r.copy()
                    r_new[i] -= 1
                    for s in triverse(r_new, i):
                        out.append([l[c]] + s)
            if len(out) == 0: return [[l[c]]]
            return out
        r = list(d.values())
        out = []
        for i in range(len(l)):
            r_new = r.copy()
            r_new[i] -= 1
            out += triverse(r_new,i)
        return out

# @lc code=end

