class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        available = []
        pending = []

        for i in range(len(tasks)):
            heapq.heappush(pending, [tasks[i][0], tasks[i][1], i])

        time = 1
        res = []

        while pending or available:
            while pending and pending[0][0] <= time:
                enqueueTime, processingTime, index = heapq.heappop(pending)
                heapq.heappush(available, [processingTime, index])

            if not available :
                time = pending[0][0]
                continue

            processingTime, index = heapq.heappop(available)
            time += processingTime
            res.append(index) 
            

        return res