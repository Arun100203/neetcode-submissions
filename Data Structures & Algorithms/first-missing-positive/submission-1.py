class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        last = len(nums)
        s = set(nums)
        for i in range(1, last+1):
            if i not in s:
                return i

        return last+1