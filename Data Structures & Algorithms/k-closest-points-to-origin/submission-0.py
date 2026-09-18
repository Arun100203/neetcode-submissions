class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        h = []

        for po in points:
            dis = po[0]**2 + po[1]**2
            heapq.heappush(h, [-1*dis, po])
            if len(h) > k:
                heapq.heappop(h)

        res = []
        while h:
            dis, po = heapq.heappop(h)
            res.append(po)

        return res