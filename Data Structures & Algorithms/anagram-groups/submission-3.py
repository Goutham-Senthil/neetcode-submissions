class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = defaultdict(list)

        for word in strs:
            chars = [0]*26

            for c in word:
                chars[(ord(c)-ord('a'))] +=1
            
            key = tuple(chars)
            hashmap[key].append(word)
        
        res = []
        for k in hashmap:
            res.append(hashmap[k])
        
        return res