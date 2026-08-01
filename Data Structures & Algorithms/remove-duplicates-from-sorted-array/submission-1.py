class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = set(nums)

        nums[0:len(temp)] = sorted(temp)
        print(nums)
        return len(temp)