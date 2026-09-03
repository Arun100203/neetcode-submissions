class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.fun(nums, 0, res, [])
        return res

    def fun(self, nums, i, res, subset):
        if i >= len(nums):
            # print(subset)
            res.append(subset.copy())
            return

        subset.append(nums[i])
        self.fun(nums, i+1, res, subset)

        subset.pop()
        self.fun(nums, i+1, res, subset)

