#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start

'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        stack = []
        count = 0
        string = ''
        max_c = 0
        max_s = ''
        for i in range(len(s)):
            if len(stack) == 0: stack.append(s[i])
            else:
                if stack[len(stack) - 1] == s[i]:
                    count += 1
                    string = string + s[i]
                    string = stack.pop() + string
                    if count > max_c:
                        max_c = count
                        max_s = string
                elif stack[len(stack) - 1] == s[i]:
                else:
                    stack.append(s[i])
                    count = 0
        return max_c
'''            

class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        @cache
        def dp(i: int, j:int) -> int:
            #print(s[j:i+1])
            if i == j:
                return 1
            if i == j + 1 and s[i] == s[j]:
                return 2
            elif i == j + 1:
                return 0
            p = dp(i - 1, j + 1)
            if s[i] == s[j] and p != 0:
                return p + 2
            return 0
        max_p = 0
        max_ij = (-1,-1)
        for j in range(l):
            for i in range(j, l):
                if i - j + 1 > max_p and s[i] == s[j]:
                    p = dp(i, j)
                    if max_p < p:
                        max_p = p
                        max_ij = (i,j)
        return s[max_ij[1]:max_ij[0]+1]
                
class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        @cache
        def dp(i: int, j:int) -> bool:
            if s[i] != s[j]:
                return False
            if i - j <= 1:
                return True
            p = dp(i - 1, j + 1)
            return p
        max_p = 0
        max_ij = (-1,-1)
        for j in range(l):
            if j + max_p < l:
                for i in range(j + max_p, l):
                    if s[i] == s[j]:
                        if dp(i, j):
                            max_p = i - j + 1
                            max_ij = (i,j)
        return s[max_ij[1]:max_ij[0]+1]

# manacher algo
class Solution:
    def longestPalindrome(self, s: str) -> str:
        s = '#' + '#'.join(s) + '#'
        p = [0] * len(s)
        max_right, max_center = 0, 0
        max_radius, max_c = 0, 0
        for i in range(len(s)):
            if i < max_right:
                p[i] = min(max_right - i, p[max_center*2 - i])
            while i + p[i] + 1 < len(s) and i - p[i] - 1 >= 0 and s[i + p[i] + 1] == s[i - p[i] - 1]:
                p[i] += 1
            if i + p[i] > max_right:
                max_center = i
                max_right = max_center + p[i]
        for i in range(len(p)):
            if max_radius < p[i]:
                max_radius = p[i]
                max_canter = i
        return ''.join(s[max_canter - max_radius: max_canter + max_radius + 1].split('#'))

# @lc code=end

