class Solution:
    def isAlienSorted(self, word: List[str], order: str) -> bool:
        

        order_map = {ch:i for i,ch in enumerate(order)}

        for w1,w2 in zip(word[:],word[1:]):
            
            for i in range(len(w1)):
                if i == len(w2):
                    return False
                
                if w1[i] != w2[i]:
                    if order_map[w1[i]] > order_map[w2[i]]:
                        return False
                    break

        return True