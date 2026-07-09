class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            org = i
            i = sorted(i)
            i = "".join(i)
            # print(org, i, d)
            if i in d:
                d[i].append(org)
            else:
                d[i] = [org]

        return list(d.values())
