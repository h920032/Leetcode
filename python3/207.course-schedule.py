#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = {}
        for i in range(numCourses):
            d[i] = []
        for p in prerequisites:
            d[p[0]].append(p[1])
        visited_set = set()
        is_check = set()
        def dfs(n):
            if n in visited_set: return False
            if n in is_check: return True
            visited_set.add(n)
            result = True
            for c in d[n]:
                result &= dfs(c)
                if not result: break
            visited_set.remove(n)
            is_check.add(n)
            return result
        out = True
        for c in range(numCourses):
            out &= dfs(c)
            if not out: return False
        return True
                
# @lc code=end

