class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)

        if n < m:
            return ""
        
        if s == t:
            return s

        dt = {}
        for i in t:
            dt[i] = dt.get(i, 0) + 1

        i = 0
        j = 0
        ans = (float('inf'), i, j)
        
        while j < n:
            # print(i, j, dt)
            char = s[j]

            if char in dt:
                dt[char] -= 1

            while self.fun(dt):
                left_char = s[i]
                if left_char in dt:
                    dt[left_char] += 1
                if ans[0] > j - i + 1:
                    ans = (j-i+1, i, j)
                i += 1
    
            j += 1

        while self.fun(dt) and i < n:
            left_char = s[i]
            if left_char in dt:
                dt[left_char] += 1
            if ans[0] > j - i + 1:
                ans = (j-i+1, i, j)
            i += 1

        return s[ans[1]:ans[2]+1] if ans[0] != float('inf') else ""

    
    def fun(self, dt):
        for i in dt:
            if dt[i] > 0:
                return False

        return True
            
                