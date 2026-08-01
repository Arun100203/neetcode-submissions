class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        temp_left = nums[:len(nums) - k]
        temp_right = nums[len(nums) - k:]

        nums[:] = temp_right + temp_left
        