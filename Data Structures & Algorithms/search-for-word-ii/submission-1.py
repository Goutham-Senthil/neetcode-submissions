class TrieNode:
    def __init__(self):
        self.children = {}
        self.eoW = False

class TrieNode:
    def __init__(self):
        self.children = {}
        self.eoW = False
    
    def addWord(self,word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.eoW = True
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        

        root = TrieNode()
        res = []
        for word in words:
            root.addWord(word)


        ROWS , COLS = len(board) , len(board[0])
        res , visit = set() , set()

        def backtrack(r,c,word,node):
            if (r<0 or c<0 or r>=ROWS or c>= COLS or (r,c) in visit or board[r][c] not in node.children):
                return 
            
            visit.add((r,c))
            node = node.children[board[r][c]]
            word+= board[r][c]
            if node.eoW:
                res.add(word)
            
            backtrack(r+1,c,word,node)
            backtrack(r-1,c,word,node)
            backtrack(r,c+1,word,node)
            backtrack(r,c-1,word,node)
            visit.remove((r,c))
            
        for r in range(ROWS):
            for c in range(COLS):
                backtrack(r,c,"",root)
        
        return list(res)
