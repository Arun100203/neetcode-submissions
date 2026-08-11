class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)

        if n < m:
            return ""
        
        if s == t:
            return s

        dt = {}
        ds = {}
        for i in t:
            dt[i] = dt.get(i, 0) + 1

        i = 0
        j = 0
        ans = (float('inf'), i, j)
        need = len(dt)
        have = 0
        while j < n:

            ds[s[j]] = ds.get(s[j], 0) + 1

            if s[j] in dt and ds[s[j]] == dt[s[j]]:
                have += 1

            while have == need:

                if ans[0] > j - i + 1:
                    ans = (j - i + 1, i, j)

                ds[s[i]] -= 1
                

                if s[i] in dt and ds[s[i]] < dt[s[i]]:
                    have -= 1

                i += 1

            j += 1

        return s[ans[1]:ans[2]+1] if ans[0] != float('inf') else ""

    

            
                