class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        return nums[len(nums)//2]