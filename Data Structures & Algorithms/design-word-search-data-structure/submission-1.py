class TrieNode():
    def __init__(self):
        self.children = {}
        self.eoW = False 
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.eoW = True
        return

    def search(self, word: str) -> bool:


        def dfs(word,root):

            curr = root
            for i,c in enumerate(word):
                if c!='.' and c not in curr.children:
                    return False
                elif c == '.':
                    for child in curr.children.values():
                        if dfs(word[i+1:],child):
                            return True
                    return False
                else:
                    curr = curr.children[c]
            return curr.eoW
        val = dfs(word,self.root)
        if not val:
            print(word)
        return val


        
