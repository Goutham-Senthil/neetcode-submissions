class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        L = 0 
        R = n - 1

        water = 0

        while L < R:
            
            area = (R - L) * min(heights[L],heights[R])

            water = max(area,water)

            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1        
        return water