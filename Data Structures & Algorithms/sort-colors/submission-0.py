class Solution:
    def sortColors(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr[:] = self.merge_sort(arr)
        
    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left, right = self.merge_sort(arr[:mid]), self.merge_sort(arr[mid:])
        
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
        
    # def sort(self, nums):
    #     if len(nums) <= 1:
    #         return nums

    #     mid = len(nums)//2
    #     left, right = self.sort(nums[mid:]), self.sort(nums[:mid])

    #     i, j = 0, 0
    #     res = []
    #     while i<len(left) and j<len(right):
    #         if left[i] < right[j]:
    #             res.append(left[i])
    #             i+=1
    #         else:
    #             res.append(right[j])
    #             j+=1 

    #     res.extend(left[i:])
    #     res.extend(right[j:])
    #     print(left, right, res)
    #     return res
