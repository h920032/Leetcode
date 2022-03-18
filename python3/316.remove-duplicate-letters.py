#
# @lc app=leetcode id=316 lang=python3
#
# [316] Remove Duplicate Letters
#

# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        min_index = -1
        out = ""
        d = {}
        for i in range(min_index + 1, len(s)):
            if s[i] not in d: d[s[i]] = 0
        while d:
            for i in range(min_index + 1, len(s)):
                if s[i] in d: d[s[i]] += 1
            min_c = 'z'
            for i in range(min_index + 1, len(s)):
                if min_c > s[i] and s[i] in d:
                    flag = True
                    for j in d:
                        if d[j] == 0:
                            flag = False
                            break
                    if flag:
                        min_c = s[i]
                        min_index = i
                if s[i] in d:d[s[i]] -= 1
            d.pop(min_c)
            out += min_c
        return out

# recirsive
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if not s: return ''
        d = {}
        min_index = 0
        for i in range(len(s)):
            if s[i] in d: d[s[i]] += 1
            else: d[s[i]] = 1
        for i in range(len(s)):
            if s[i] < s[min_index]:
                min_index = i
            d[s[i]] -= 1
            if d[s[i]] == 0: break
        return s[min_index] + self.removeDuplicateLetters(s[min_index:].replace(s[min_index], ""))

# with stack
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        d = {}
        for i in range(len(s)):
            if s[i] in d: d[s[i]] += 1
            else: d[s[i]] = 1
        for i in range(len(s)):
            if s[i] not in stack:
                while len(stack) != 0 and stack[-1] > s[i] and d[stack[-1]] > 0:
                    stack.pop()
                stack.append(s[i])
            d[s[i]] -= 1
        return "".join(stack)

# @lc code=end

