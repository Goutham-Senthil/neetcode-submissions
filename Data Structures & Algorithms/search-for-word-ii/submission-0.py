class TrieNode:
    def __init__(self):
        self.children = {}
        self.eoW = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self,word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.eoW = True
    
    def prefixWord(self,word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True

    def isWord(self,word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.eoW
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        

        trie = Trie()
        res = []
        for word in words:
            trie.addWord(word)


        ROWS , COLS = len(board) , len(board[0])
        res , visit = set() , set()

        def backtrack(r,c,word):
            if (r<0 or c<0 or r>=ROWS or c>= COLS or (r,c) in visit or not trie.prefixWord(word+board[r][c])):
                return 
            
            visit.add((r,c))
            # node = node.children[board[r][c]]
            word+= board[r][c]
            if trie.isWord(word):
                res.add(word)
            
            backtrack(r+1,c,word)
            backtrack(r-1,c,word)
            backtrack(r,c+1,word)
            backtrack(r,c-1,word)
            visit.remove((r,c))
            
        for r in range(ROWS):
            for c in range(COLS):
                backtrack(r,c,"")
        
        return list(res)
