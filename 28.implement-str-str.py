#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lh = len(haystack)
        ln = len(needle)
        if ln == 0:
            return 0
        elif lh == 0 and ln != 0:
            return -1
        for i in range(lh - ln + 1):
            if haystack[i:i+ln] == needle:
                return i
        return -1


'''
[0,1,2,3,4,5,6,7,8]
[A,B,C,A,B,C,B,A,B]
[0,0,0,1,2,3,0,1,2]

a,a,a,a

[b,b,a]
[0,1,0]


'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lh = len(haystack)
        ln = len(needle)
        if ln == 0:
            return 0
        elif lh == 0 and ln != 0:
            return -1
        
        f = [-1] * ln
        for i in range(1,ln):
            r = f[i-1]
            while needle[i] != needle[r] and r != 0:
                r = f[r-1]
            if needle[i] == needle[r]:
                f[i] = r + 1
            else:
                f[i] = 0

        i = 0
        r = 0
        while i < lh:
            if haystack[i] != needle[r]:
                if r == 0:
                    i += 1
                    continue
                else:
                    r = f[r-1]
            else:
                i += 1
                r += 1
            
            if r == ln:
                return i - r

        return -1


# @lc code=end

