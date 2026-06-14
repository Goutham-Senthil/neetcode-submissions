class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0 
        r = len(nums) - 1
        # 2,2,2,3,1

        while l<=r:
            mid = (l+r)//2

            if nums[mid] == target:
                return True
            elif nums[mid] == nums[l]: # undeterministic
                l += 1
            elif nums[l] <= nums[mid]: # somewhere here ?
                if nums[l] > target or nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid
                else:
                    l = mid + 1 
        
        return False