class Solution:
    def mySqrt(self, x: int) -> int:
        n = x//2

        if x == 1 or x == 2 or x == 3:
            return 1

        left = 1
        right = n 
        while left <= right:

            mid = left + (right-left) // 2
            # print(left, right, mid)
            
            power = mid*mid
            if power == x:
                return mid
            elif power > x:
                right = mid - 1
            else:
                left = mid + 1
        
        return right