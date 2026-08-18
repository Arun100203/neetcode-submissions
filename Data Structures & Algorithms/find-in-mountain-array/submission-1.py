class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        midPos, midValue = self.findMid(mountainArr)

        if midValue == target:
            return midPos
        
        elePresinLeft = self.findEle(mountainArr, target, False)

        if elePresinLeft == -1:
            return self.findEle(mountainArr, target, True)

        return elePresinLeft

    def findEle(self, mountainArr, target, right):
        n = mountainArr.length()

        l, r = 0, n-1

        while l <= r:
            mid = l + (r-l)//2

            midVal = mountainArr.get(mid)
            if midVal == target:
                return mid
            elif midVal < target:
                if right:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if right:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1

    def findMid(self, mountainArr):
        n = mountainArr.length()

        l, r = 0, n-1

        while l<=r:

            mid = l + (r-l)//2

            midEle = mountainArr.get(mid)
            if mid + 1 < n and mid - 1 >= 0:
                midBef = mountainArr.get(mid-1)
                midAft = mountainArr.get(mid+1)

                if midBef < midEle and midEle > midAft:
                    return mid, midEle
                elif midBef < midEle and midEle < midAft:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if mid + 1 >= n:
                    midBef = mountainArr.get(mid-1)
                    if midBef > midEle:
                        return mid, midEle
                    else:
                        return -1, -1
                else:
                    midAft = mountainArr.get(mid+1)
                    if midAft > midEle:
                        return mid, midEle
                    else:
                        return -1, -1

            