#
# @lc app=leetcode id=1209 lang=python3
#
# [1209] Remove All Adjacent Duplicates in String II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        match_set = set()
        new_s = ''
        for i in range(26):
            match_set.add(chr(ord('a') + i) * k)
        for c in s:
            new_s += c
            l = len(new_s)
            if l >= k and new_s[l - k:] in match_set:
                    new_s = new_s[:l - k]
        return new_s

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [1]
        new_s = s[0]
        for c in range(1, len(s)):
            if len(new_s) == 0:
                stack.append(1)
            elif s[c] == new_s[-1]: stack[-1] += 1
            else: stack.append(1)
            new_s += s[c]
            if stack[-1] == k:
                new_s = new_s[:len(new_s) - k]
                stack.pop()
        return new_s

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        j = 0
        stack = []
        new_s = [c for c in s]
        for i in range(len(new_s)):
            new_s[j] = new_s[i]
            if j == 0 or new_s[j] != new_s[j - 1]:
                stack.append(1)
            else:
                stack[-1] += 1
                if stack[-1] == k:
                    stack.pop()
                    j -= k
            j += 1
        return ''.join(new_s[:j])

# @lc code=end

