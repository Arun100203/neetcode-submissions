class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        h1 = []
        h2 = []
        max_dis = 0
        for i in trips:
            if i[0] > capacity:
                return False
            heapq.heappush(h1, (i[1], i[2], i[0]))
            max_dis = max(max_dis, i[2])

        pre = None
        distance = h1[0][0]
        cur_cap = 0
        h2 = []
        while h1 and distance<=max_dis:
            
            
            
            # print("before",cur, h1, h2, distance, cur_cap)

            while h2 and distance == h2[0][0]:
                cur_cap -= h2[0][2]
                heapq.heappop(h2)

            # print("After",cur, h1, h2, distance, cur_cap)
            while h1 and distance == h1[0][0]:
                cur = heapq.heappop(h1)
                cur_cap += cur[2]
                heapq.heappush(h2, (cur[1], cur[0], cur[2]))
                if cur_cap > capacity:
                    return False


            distance += 1

        return True
