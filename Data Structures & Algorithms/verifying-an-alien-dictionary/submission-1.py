class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        

        order_map = {ch:i for i,ch in enumerate(order)}

        def compare(word):
            to_return = [order_map[c] for c in word]
            print(to_return)
            return to_return

        alien_words = sorted(words,key = compare)

        return alien_words == words