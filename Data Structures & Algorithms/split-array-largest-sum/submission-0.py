class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = 0
        for i in nums:
            right += i
        # ans = left
        while left <= right:
            mid = left + (right - left) // 2

            count = self.fun(nums, mid)
            # print(mid, count, left, right)
           
            if count > k:
                left = mid + 1
            else:
                right = mid - 1

        return left

    def fun(self, nums, mid):
        ans = 1          
        temp_mid = 0     
        
        for weight in nums:
            if temp_mid + weight > mid:
                ans += 1             
                temp_mid = weight    
            else:
                temp_mid += weight
        

        return ans

