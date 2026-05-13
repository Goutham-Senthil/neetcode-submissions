class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q = collections.deque()
        heap = []

        cycles = 0
        t_C = Counter(tasks)

        print(t_C)

        for character in t_C:
            heapq.heappush(heap,-t_C[character])


        i = 0
        while heap or q:
            i+=1
            if not heap:
                i = q[0][1]
            else:
                process = heapq.heappop(heap)
                # process is a negative value
                process+=1
                # i+n is the time it can be 
                # popped out
                if process !=0:
                    q.append([process,i+n])
            if q and q[0][1] == i:
                back_to_heap,_ = q.popleft()
                heapq.heappush(heap,back_to_heap)
            
            
        return i