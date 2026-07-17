class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        curr = 1
        prev = 0
        for i in range(1, n+1):
            prev, curr = curr, curr+prev
            # print(prev, curr)

        return curr