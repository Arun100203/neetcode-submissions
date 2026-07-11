class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 1
        nums = set(nums)
        if len(nums) == 1:
            return 1
        if len(nums) == 0:
            return 0
        for i in nums:
            if i+1 in nums and i-1 not in nums:
                temp = i+1
                maxi = 1
                while temp in nums:
                    # print(maxi, temp)
                    maxi += 1
                    temp += 1
                ans = max(ans, maxi)

        return ans