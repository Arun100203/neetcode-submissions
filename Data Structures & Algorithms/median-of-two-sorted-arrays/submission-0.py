class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)

        half = (n+m)//2

        A, B = nums1, nums2

        if m < n:
            B, A = nums1, nums2

        l, r = 0, len(A) - 1
        while True:
            i = (l+r)//2
            j = half - i -2

            ALeft = A[i] if i>=0 else float("-infinity")
            BLeft = B[j] if j>=0 else float("-infinity")
            ARight = A[i+1] if i+1 < len(A) else float('infinity')
            BRight = B[j+1] if j+1 < len(B) else float('infinity')

            if ALeft <= BRight and BLeft <= ARight:
                if (n+m)%2:
                    return min(ARight, BRight)

                return (min(ARight, BRight) + max(ALeft, BLeft)) / 2

            if ALeft > BRight:
                r = i - 1
            else:
                l = i + 1