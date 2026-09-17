class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = stones
        heapq.heapify_max(heap)

        while len(heap) >= 2:
            dif = heapq.heappop_max(heap) - heapq.heappop_max(heap)
            if dif != 0:
                heapq.heappush_max(heap, dif)

            
        return heap and heap[-1] or 0