class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}

        i = 0
        ans = 0
        if len(s) <= 1:
            return len(s)

        for j in range(len(s)):

            if s[j] in d and d[s[j]] >= i:
                i = d[s[j]] + 1

            d[s[j]] = j

            ans = max(ans, j - i + 1)

        return ans