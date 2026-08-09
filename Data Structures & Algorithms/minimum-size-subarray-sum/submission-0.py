class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf')

        left = 0
        right = 0
        n = len(nums)
        sm = 0

        while right < n:
            sm += nums[right]

            while sm >= target:
                ans = min(ans, right - left + 1)

                sm -= nums[left]
                left += 1

            right += 1            
        
        return ans if ans != float('inf') else 0