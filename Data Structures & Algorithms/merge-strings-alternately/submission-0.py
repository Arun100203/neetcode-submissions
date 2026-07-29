class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        n, m = len(word1), len(word2)
        res = []
        while i < n and j < m:
            res.append(word1[i])
            res.append(word2[j])

            i += 1
            j += 1

        if i == n:
            res.append(word2[j:m])
        else:
            res.append(word1[i:n])

        # print(res)

        return "".join(res)