class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1)
        for i in range(n+1):
            res = 0
            j = i
            while i > 0:
                i = i & (i - 1)
                res += 1
            ans[j] = res
        return ans