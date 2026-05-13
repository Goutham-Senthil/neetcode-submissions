class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        area = 0

        for i,h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                index,val = stack.pop()
                area = max(area,val*(i-index))
                start = index
            stack.append((start,h))
        
        for i,h in stack:
            area = max(area,h*(len(heights)-i))
        
        return area
                