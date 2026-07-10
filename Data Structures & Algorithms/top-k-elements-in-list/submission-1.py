class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i in d:
                d[i] +=1
            else:
                d[i] = 1

        d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
        res = list(d.keys())
        return res[:k]
        