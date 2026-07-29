class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums2 = nums2[0:n]
        temp = nums1[0:m]
        temp.extend(nums2)
        nums1[:] = temp
        nums1.sort()
