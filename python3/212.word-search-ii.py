#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

# @lc code=start
class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.word = None
    def insert(self, word, i):
        if i == len(word):
            self.word = word
            return None
        if self.child[ord(word[i]) - ord('a')] == None:
            self.child[ord(word[i]) - ord('a')] = TrieNode()
        self.child[ord(word[i]) - ord('a')].insert(word, i+1)

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = TrieNode()
        out = []
        for w in words:
            trie.insert(w, 0)
        
        is_used = [[0] * len(board[0]) for i in range(len(board))]
        
        def traverse(t, i, j):
            F = [[1,0],[-1,0],[0,1],[0,-1]]
            if t.child[ord(board[i][j]) - ord('a')] != None:
                for f in F:
                    if f[0] + i < len(board) and f[0] + i >= 0 and j + f[1] < len(board[0]) and j + f[1] >= 0 and is_used[i + f[0]][j + f[1]] != 1:
                        is_used[i + f[0]][j + f[1]] = 1
                        traverse(t.child[ord(board[i][j]) - ord('a')], i + f[0], j + f[1])
                        is_used[i + f[0]][j + f[1]] = 0
                if t.child[ord(board[i][j]) - ord('a')].word != None:
                    out.append(t.child[ord(board[i][j]) - ord('a')].word)
                    all_none = True
                    for c in t.child[ord(board[i][j]) - ord('a')].child:
                        if c != None:
                            all_none = False
                    t.child[ord(board[i][j]) - ord('a')].word = None
                    if all_none: t.child[ord(board[i][j]) - ord('a')] = None
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if trie.child[ord(board[i][j]) - ord('a')] != None:
                    is_used[i][j] = 1
                    traverse(trie, i, j)
                    is_used[i][j] = 0
        return out
                
# @lc code=end

