#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        d = {}
        def dfs(node):
            if not node: return None
            if node not in d:
                new = Node()
                d[node] = new
                new.val = node.val
                for n in node.neighbors:
                    new.neighbors.append(dfs(n))
                return new
            else:
                return d[node]
        return dfs(node)
                
# @lc code=end

