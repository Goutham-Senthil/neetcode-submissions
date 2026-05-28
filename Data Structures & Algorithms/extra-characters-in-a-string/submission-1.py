class TrieNode():
    def __init__(self):
        self.children = {}
        self.minlength = float('-inf')
        self.eoW = False

class Trie():
    def __init__(self):
        self.root = TrieNode()
        self.root.minlength = 0

    def addWord(self,word):
        curr = self.root
        
        for c in word:
            if c not in curr.children:
                
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.eoW = True
        curr.minlength = len(word)
    
    def search(self,word):
        curr = self.root
        best = curr.minlength

        for c in word:
            if c not in curr.children:
                break
            curr = curr.children[c]
            if curr.eoW:
                best = max(best,curr.minlength)
        print(best)
        return len(word) - best


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        trie = Trie()

        dp = {len(s): 0}


        for w in dictionary:
            trie.addWord(w)

        def dfs(i):
            if i in dp:
                return dp[i]
            res = 1 + dfs(i + 1)
            curr = trie.root
            for j in range(i, len(s)):
                if s[j] not in curr.children:
                    break
                curr = curr.children[s[j]]
                if curr.eoW:
                    res = min(res, dfs(j + 1))

            dp[i] = res
            return res

        return dfs(0)





