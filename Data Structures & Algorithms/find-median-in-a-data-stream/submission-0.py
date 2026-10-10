class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []

        

    def addNum(self, num: int) -> None:
        
        heapq.heappush(self.maxheap, -1 * num)

        n = heapq.heappop(self.maxheap)
        heapq.heappush(self.minheap, -1 * n)

        if len(self.maxheap) < len(self.minheap):
            n = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -1 * n)

        # print(self.minheap, self.maxheap)

    def findMedian(self) -> float:
        if len(self.maxheap) == len(self.minheap):
            return ((-1 * self.maxheap[0]) + self.minheap[0]) / 2.0

        return -1*self.maxheap[0]

        
        