#
# @lc app=leetcode id=1202 lang=python3
#
# [1202] Smallest String With Swaps
#

# @lc code=start
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        p_set = {}
        for p in pairs:
            if p[0] in p_set:
                p_set[p[0]].append(p[1])
            else:
                p_set[p[0]] = [p[1]]
            if p[1] in p_set:
                p_set[p[1]].append(p[0])
            else:
                p_set[p[1]] = [p[0]]
        
        target_set = []
        visited = set()
        
        def find(n, s):
            if n in visited: return
            s.add(n)
            visited.add(n)
            for i in p_set[n]:
                find(i, s)
        find_set = []
        
        for k in p_set:
            if k not in visited:
                t = set()
                find(k, t)
                find_set.append(t)
        s_new = [c for c in s]
        
        for sub_set in find_set:
            I = sorted(list(sub_set))
            l = []
            for i in I:
                l.append(s_new[i])
            l = sorted(l)
            for i in range(len(I)):
                s_new[I[i]] = l[i]
        
        return ''.join(s_new)
                
# @lc code=end

