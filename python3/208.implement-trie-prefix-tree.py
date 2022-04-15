#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
# Recursive
class Trie:
    def __init__(self):
        self.child = [None] * 26
        self.word = False

    def insert(self, word: str) -> None:
        if len(word) == 0:
            self.word = True
        elif not self.child[ord(word[0]) - ord('a')]:
            self.child[ord(word[0]) - ord('a')] = Trie()
            self.child[ord(word[0]) - ord('a')].insert(word[1:])
        else:
            self.child[ord(word[0]) - ord('a')].insert(word[1:])

    def search(self, word: str) -> bool:
        if len(word) == 0: return self.word
        if not self.child[ord(word[0]) - ord('a')]: return False
        else: return self.child[ord(word[0]) - ord('a')].search(word[1:])

    def startsWith(self, prefix: str) -> bool:
        if len(prefix) == 0: return True
        if not self.child[ord(prefix[0]) - ord('a')]: return False
        else: return self.child[ord(prefix[0]) - ord('a')].startsWith(prefix[1:])

# Iterative
class Trie:
    def __init__(self):
        self.child = [None] * 26
        self.word = False

    def insert(self, word: str) -> None:
        i = 0
        t = self
        while i < len(word):
            c = ord(word[i]) - ord('a')
            if not t.child[c]:
                t.child[c] = Trie()
            t = t.child[c]
            i += 1
        t.word = True

    def search(self, word: str) -> bool:
        i = 0
        t = self
        while i < len(word):
            c = ord(word[i]) - ord('a')
            if not t.child[c]: return False
            t = t.child[c]
            i += 1
        return t.word

    def startsWith(self, prefix: str) -> bool:
        i = 0
        t = self
        while i < len(prefix):
            c = ord(prefix[i]) - ord('a')
            if not t.child[c]: return False
            t = t.child[c]
            i += 1
        return True

# with dict
class Trie:
    def __init__(self):
        self.child = {}
        self.word = False

    def insert(self, word: str) -> None:
        t = self
        for c in word:
            if c not in t.child: t.child[c] = Trie()
            t = t.child[c]
        t.word = True

    def search(self, word: str) -> bool:
        t = self
        for c in word:
            if c not in t.child: return False
            t = t.child[c]
        return t.word

    def startsWith(self, prefix: str) -> bool:
        t = self
        for c in prefix:
            if c not in t.child: return False
            t = t.child[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

