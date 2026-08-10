class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = 0
        for i in weights:
            right += i
        # ans = left
        while left <= right:
            mid = left + (right - left) // 2

            count = self.fun(weights, mid)
            # print(mid, count, left, right)
           
            if count > days:
                left = mid + 1
            else:
                right = mid - 1

        return left

    def fun(self, weights, mid):
        ans = 1          
        temp_mid = 0     
        
        for weight in weights:
            if temp_mid + weight > mid:
                ans += 1             
                temp_mid = weight    
            else:
                temp_mid += weight
        

        return ans
        