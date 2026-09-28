class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        fre = [0] *26
        for i in tasks:
            fre[ord(i)-ord('A')] -= 1

        # print(fre)
        h = []
        for i in fre:
            if i != 0:
                heapq.heappush(h, i)

        print(h)
        q = deque()
        time = 0

        while h or q:
            if not h:
                time = q[0][1]
            else:
                t = heapq.heappop(h)
                t += 1
                if t != 0:
                    q.append([t, time+n])

            if q and q[0][1] == time:
                t1 = q.popleft()
                heapq.heappush(h, t1[0])

            time += 1

            
        return time