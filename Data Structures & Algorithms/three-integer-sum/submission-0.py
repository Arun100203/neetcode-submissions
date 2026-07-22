class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        d = {}
        seen = [0]*n
        for i in range(n):
            if nums[i] in d:
                d[nums[i]].append(i)
            else:
                d[nums[i]] = [i]

        # print(d)
        ans = set()
        for i in range(n):
            for j in range(i + 1, n):
                target = -1 * (nums[i] + nums[j])
                
                if target in d:
                    if self.does_d(d, target, j):
                        triplet = tuple(sorted([nums[i], nums[j], target]))
                        ans.add(triplet)

        return [list(t) for t in ans]

    def does_d(self, d, target, j):
        index_list = d[target]
        for idx in index_list:
            if idx > j:
                return True
        return False