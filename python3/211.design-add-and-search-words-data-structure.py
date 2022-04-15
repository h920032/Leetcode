#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start
class WordDictionary:
    def __init__(self):
        self.child = {}
        self.word = False

    def addWord(self, word: str) -> None:
        t = self
        for c in word:
            if c not in t.child: t.child[c] = WordDictionary()
            t = t.child[c]
        t.word = True

    def search(self, word: str) -> bool:
        if len(word) == 0: return self.word
        if word[0] in self.child: return self.child[word[0]].search(word[1:])
        out = False
        if word[0] == '.':
            for k in list(self.child.keys()):
                out = out or self.child[k].search(word[1:])
        return out        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

