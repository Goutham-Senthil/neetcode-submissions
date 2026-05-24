class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        mini = n =len(nums)
        summ = nums[l]
        possible_sum = sum(nums)
        if possible_sum < target:
            return 0
        for r in range(n):
            if r == 0:
                summ+=0
            else:
                summ+=nums[r]
            if summ >= target:
                print(nums[l:r+1])
                mini = min(mini,r-l+1)
                while summ >= target:
                    mini = min(mini,r-l+1)
                    summ-=nums[l]
                    l+=1
        if summ >= target:
            # print("yes")
            mini = min(mini,r-l+1)
        return mini