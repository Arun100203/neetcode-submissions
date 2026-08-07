class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sta = []
        d = {}
        n = len(speed)
        for i in range(n):
            d[position[i]] = speed[i]
        # print(d)
        position.sort(reverse=True)
        # print(position)

        for i in position:
            time = (target-i ) / d[i]
            # print(time, sta)
            sta.append(time)
            if len(sta) > 1 and sta[-1] <= sta[-2]:
                sta.pop() 
                                
        # print(sta)
        return len(sta)



        