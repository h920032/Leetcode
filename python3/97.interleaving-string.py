#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False
        @cache
        def triverse(ptr_s1, ptr_s2, ptr_s3):
            for i in range(ptr_s3, len(s3)):
                if ptr_s1 < len(s1) and ptr_s2 < len(s2) and s1[ptr_s1] == s2[ptr_s2] and s1[ptr_s1] == s3[i]:
                    return triverse(ptr_s1 + 1, ptr_s2, i + 1) or triverse(ptr_s1, ptr_s2 + 1, i + 1)
                elif ptr_s1 < len(s1) and s3[i] == s1[ptr_s1]:
                    ptr_s1 += 1
                elif ptr_s2 < len(s2) and s3[i] == s2[ptr_s2]:
                    ptr_s2 += 1
                else: return False
            return True
        return triverse(0,0,0)
                
# @lc code=end

