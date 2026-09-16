class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.q = deque(nums)
        self.n = len(nums)
        self.k = k


    def add(self, val: int) -> int:
        if self.n > len(self.q):
            self.q.pop()

        self.q.append(val)
        return heapq.nlargest(self.k, self.q)[-1]
