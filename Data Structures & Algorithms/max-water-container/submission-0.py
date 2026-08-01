class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        i = 0
        n = len(heights)
        j = n-1
        maxi = -1

        while i < j:
            maxi = max(maxi, (j - i) * min(heights[i], heights[j]))

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return maxi