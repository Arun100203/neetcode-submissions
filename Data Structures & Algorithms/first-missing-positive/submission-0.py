class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        last = pow(2, 31) - 1
        s = set(nums)
        for i in range(1, last):
            if i not in s:
                return i

        return last