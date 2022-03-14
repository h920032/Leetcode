#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        l = path.split('/')
        out_list = []
        for i in l:
            if len(i) == 0 or i == ".":
                continue
            elif i == '..':
                if len(out_list) != 0:
                    out_list.pop()
            else:
                out_list.append(i)
        return "/" + "/".join(out_list)
        
# @lc code=end

