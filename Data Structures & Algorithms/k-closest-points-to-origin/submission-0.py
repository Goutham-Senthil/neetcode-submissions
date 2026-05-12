class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []
        

        def dist(x,y):
            return -1*math.sqrt(x**2 + y**2)

        for point in points:
            x,y = point
            heapq.heappush(heap,[dist(x,y),point])
            if len(heap)>k:
                heapq.heappop(heap)

        
        return [point for _,point in heap]