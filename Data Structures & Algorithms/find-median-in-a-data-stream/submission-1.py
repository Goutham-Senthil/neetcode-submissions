class MedianFinder:

    def __init__(self):
        # we will have 2 heaps
        # a "small" heap -> max heap 
        # a "large" heap -> min heap
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        # we by default add it to
        # to the small heap
        heapq.heappush(self.small,-1*num)


        # all values in the small heap 
        # are <= large
        if (self.small and self.large and ((-1*self.small[0]) > self.large[0])):
            val = heapq.heappop(self.small)
            heapq.heappush(self.large,-1*val)
        
        # if uneven length
        # 2 conditions 
        # 1) small > large
        if len(self.small) > len(self.large)+1:
            val = heapq.heappop(self.small)
            heapq.heappush(self.large,-1*val)

        # 2) large>small
        if len(self.large) > len(self.small)+1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small,-1*val)

    def findMedian(self) -> float:
        # 2 conditons -> 
        # either odd or even amount of data

        print(f"{self.small} and {self.large}")

        # "ODD" conditon
        if len(self.small) > len(self.large):
            return -1*self.small[0]
        
        if len(self.large) > len(self.small):
            return self.large[0]
        
        
        # "EVEN" conditon
        return (-1*self.small[0] + self.large[0])/2
        
        