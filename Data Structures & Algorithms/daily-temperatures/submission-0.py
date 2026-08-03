class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n
        sta = []
        for i in range(n):
            while sta and sta[-1][1] < temperatures[i]:
                t = sta.pop()
                res[t[0]] = i - t[0]
            
            sta.append((i, temperatures[i]))

        return res
