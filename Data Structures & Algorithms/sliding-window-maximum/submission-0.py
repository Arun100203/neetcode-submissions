class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i = 0
        j = k

        maxi = -10001

        while i < k:
            maxi = max(nums[i], maxi)
            i+=1

        # print(maxi, i)
        res = [0]*(len(nums)-k+1)
        res[0] = maxi

        i, j = 1, k
        while j < len(nums) and i < len(nums) - k +1:
            maxi = max(nums[i:j+1])
            
            # print(maxi)
            # print(i, j)
            res[i] = maxi
            i += 1
            j += 1
        return res