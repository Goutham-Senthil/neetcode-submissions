class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums) 
        goal = n - 1

        for i in reversed(range(n)):
            if i+nums[i]>=goal:
                goal = i
        return goal == 0