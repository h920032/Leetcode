#
# @lc app=leetcode id=1029 lang=python3
#
# [1029] Two City Scheduling
#

# @lc code=start
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        a_costs = []
        b_costs = []
        switch = 0
        for c in costs:
            if c[0] < c[1]:
                a_costs.append(c)
            else:
                b_costs.append(c)
        if len(b_costs) > len(a_costs):
            a_costs, b_costs = b_costs, a_costs
            switch = 1
        n = len(a_costs) - len(costs)//2
        a_costs.sort(key=lambda a:max(a[0], a[1]) - min(a[0], a[1]))
        b_costs += a_costs[:n]
        a_costs = a_costs[n:]
        result = 0
        for c in a_costs:
            result += c[0 + switch]
        for c in b_costs:
            result += c[1 - switch]
        return result
                
# @lc code=end

