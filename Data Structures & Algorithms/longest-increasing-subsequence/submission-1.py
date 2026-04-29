class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # inutuion 
        # longest subsequence we can make
        # if we end here
        n = len(nums)
        dp = [1]*(n) # by default we can make one only


        # it is "increasing"
        # what does that mean ? 
        # we can use binary search


        tails = []
        for n in nums:
            if not tails:
                tails.append(n)
                continue
            i = self.binSearch(tails,n)
            if i == len(tails):
                tails.append(n)
            else:
                tails[i] = n
        
        return len(tails)
    def binSearch(self, nums:List[int],target:int)->int:
        l = 0
        r = len(nums)

        while l<r:
            mid = l + (r-l)//2

            if nums[mid]<target:
                l = mid+1
            else:
                r = mid
        return l

