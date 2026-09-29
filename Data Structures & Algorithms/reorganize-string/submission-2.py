class Solution:
    def reorganizeString(self, s: str) -> str:
        h1 = []
        h2 = []
        d = {}

        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]] += 1

        res = []

        h = []
        max_fre = 0
        for i in d:
            heapq.heappush(h, (-d[i], i))
            max_fre = max(max_fre, d[i])

        if max_fre > ((len(s)+1)//2):
            return ""

        q = deque()
        time = 1
        while h or q:
            fre, ele = heapq.heappop(h)
            
            if fre != 0:
                res.append(ele)
                q.append((fre+1, ele, time+1))

            print(q and q[0][-1], res[-1])
            
            if q and q[0][-1] == time:
                fre, ele, time = q.popleft()
                heapq.heappush(h, (fre, ele))  

            time += 1

        return "".join(res)