class Solution:
    def findMin(self, nums: List[int]) -> int:

        if len(nums) == 2:
            return nums[0] if nums[0] < nums[1] else nums[1]
        
        if len(nums) == 1:
            return nums[0]
        
        n = len(nums)
        mid = n // 2
        return min(self.findMin(nums[0:mid]), self.findMin(nums[mid:n]))