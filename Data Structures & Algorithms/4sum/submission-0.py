class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        quad = []

        def kSum(k,start,target):
            if k!=2:
                for i in range(start,n - k + 1):
                    if i>start and nums[i] == nums[i-1]:
                        continue
                    quad.append(nums[i])
                    kSum(k-1,i+1,target - nums[i])
                    quad.pop()
                return
            
            l , r = start , n - 1
            while l < r:
                if nums[l] + nums[r] > target:
                    r-=1
                elif nums[l] + nums[r] < target:
                    l+=1
                else:
                    # quad.append(nums[l])
                    # quad.append(nums[r])
                    res.append(quad + [nums[l],nums[r]])
                    # quad.pop()
                    # quad.pop()
                    l+=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
            return
        kSum(4,0,target)
        return res