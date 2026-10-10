class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        sumi = 0
        n = len(nums)
        for i in range(2**n):
            index = bin(i)[2:].zfill(n)
            
            t = []
            ans = 0

            ind = 0
            for j in index:
                if j == '1':
                    ans ^= nums[ind]

                ind += 1

            sumi += ans


        return sumi

    def xor(self, nums):
        ans = 0
        for k in range(len(nums)):
            ans ^= nums[k]

        return ans