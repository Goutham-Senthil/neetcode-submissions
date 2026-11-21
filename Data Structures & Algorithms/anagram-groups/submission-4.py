class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # has do with hashmaps 
        h = {}


        for i,s in enumerate(strs):

            chars = [0] * 26 # we are going to use this as a key

            for c in s:
                index = ord(c) - ord('a')
                chars[index] += 1
            
            chars = tuple(chars)

            if chars not in h:
                h[chars] = []
            h[chars].append(i)
        


        ans = []
        for key in h:
            sublist = []
            for index in h[key]:
                sublist.append(strs[index])
            ans.append(sublist)
        
        return ans
