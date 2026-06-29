class Solution:
    def jump(self, nums: List[int]) -> int:
        q = collections.deque()
        q.append([0,0])
        seen = set()
        n = len(nums)

        while q:
            i , jumps = q.popleft()
            if i == n-1:
                return jumps
            
            for j in range(1,n):
                if j <= nums[i] and (i+j) not in seen:
                    seen.add((i+j))
                    q.append([i+j,jumps+1])
        return n-1 