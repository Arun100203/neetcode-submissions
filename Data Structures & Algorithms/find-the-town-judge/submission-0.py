class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        d = defaultdict(int)

        for i, j in trust:
            d[i] -= 1
            d[j] += 1

        for i in range(1, n+1):
            if d[i] == n-1:
                return i

        return -1