class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = right
        # while left <= right:
        #     mid = left + (right - left) // 2

        #     hour = self.fun(mid, piles, h)
        #     if hour:
        #         ans = min(ans, mid)
        #     else:
                
        while left <= right:
            mid = left + (right - left) // 2
            hour, t = self.fun(mid, piles, h)
            if hour:
                ans = min(ans, mid)
            
            if t > h:
                left = mid + 1
            else:
                right = mid - 1

        return ans


        
    def fun(self, mid, piles, h):
        t = 0

        for i in piles:
            # print(mid, t)
            if t > h:
                return False, t

            elif i <= mid:
                t += 1
            elif i % mid == 0:
                t += (i // mid)
            else:
                if int(i/mid) == 0:
                    t += 2
                else:
                    t += int(i / mid) + 1
        if t > h:
            return False, t

        return True, t