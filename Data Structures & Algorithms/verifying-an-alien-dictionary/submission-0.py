class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        

        order_map = {ch:i for i,ch in enumerate(order)}

        alien_words = sorted(words,key = lambda word:[order_map[ch] for ch in word])

        return alien_words == words