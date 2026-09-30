class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        
        h = []
        if a != 0:
            heapq.heappush(h, (-a, 'a'))
        if b != 0:
            heapq.heappush(h, (-b, 'b'))
        if c != 0: 
            heapq.heappush(h, (-c, 'c'))


        res = []
        q = deque()
        time = 1
        while h :
            fre, ele = heapq.heappop(h)

            if fre != 0 and len(res) >= 2 and res[-1] == res[-2] == ele:
                if not h:
                    break

                fre2, ele2 = heapq.heappop(h)
                res.append(ele2)

                fre2 += 1
                if fre2 < 0:
                    heapq.heappush(h, (fre2, ele2))

                heapq.heappush(h, (fre, ele))

            else:
                fre += 1
                res.append(ele)
                if fre < 0:
                    heapq.heappush(h, (fre, ele))

        return  "".join(res)