from heapq import heappush, heappop

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        N = len(tasks)

        for i in range(N):
            tasks[i].append(i)
        
        tasks.sort(key = lambda task : task[0])

        res = []
        minHeap = []

        i = 0
        currTime = tasks[0][0]

        while i < N or len(minHeap) > 0:
            while i < N and currTime >= tasks[i][0]:
                heappush(minHeap, [tasks[i][1], tasks[i][2]])
                i += 1
            
            if len(minHeap) <= 0:
                currTime = tasks[i][0]
            else:
                processTime, index = heappop(minHeap)
                currTime += processTime
                res.append(index)
            
        return res




