class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        sta = []
        
        for i in asteroids:
            des = False

            while sta and sta[-1] > 0 and i < 0:
                if abs(i) == sta[-1]:
                    sta.pop()
                    des = True
                    break
                elif abs(i) > sta[-1]:
                    sta.pop()
                    continue
                else:
                    des = True
                    break

            if not des:
                sta.append(i)

        return sta