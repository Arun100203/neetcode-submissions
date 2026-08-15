class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)

        while l<= r:
            mid = l + (r - l)//2

            count = 0
            su = 1
            for i in nums:
                if count + i <= mid:
                    count += i
                else:
                    su += 1
                    count = i
                    
                    
            if su > k:
                l = mid + 1
            else:
                r = mid -1

        return l


