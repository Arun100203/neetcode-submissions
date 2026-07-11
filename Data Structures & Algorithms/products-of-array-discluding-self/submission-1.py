class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1]*n
        # suffix = [1]*n

        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        pre = 1
        for i in range(-2, -1*(n+1), -1):
            # print(i, suffix[i+1], nums[i+1])
            pre *= nums[i+1]
            # suffix[i] = suffix[i+1] * nums[i+1]
            prefix[i] *= pre

        # print(suffix)

        # for i in range(n):
        #     nums[i] = prefix[i]*suffix[i]
        
        return prefix