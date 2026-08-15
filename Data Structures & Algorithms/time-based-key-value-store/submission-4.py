class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        t = []
        if key in self.d:
            t = self.d[key]
        else:
            self.d[key] = []

        self.d[key].append((value, timestamp))
        # print(self.d)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
            
        arr = self.d[key]

        l, r = 0, len(arr) -1

        while l <= r:
            mid = l + (r-l)//2

            if arr[mid][1] == timestamp:
                return arr[mid][0]

            elif arr[mid][1] > timestamp:
                r = mid - 1
            else:
                l = mid + 1
        

        return arr[r][0] if arr[r][1] <= timestamp else ""
