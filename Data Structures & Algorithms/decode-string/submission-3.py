class Solution:
    def decodeString(self, s: str) -> str:
        sta = []
        k = 0
        cur = ""
        for i in s:
            if i.isdigit():
                k = k*10 + int(i)
            elif i == '[':
                sta.append((cur, k))
                cur = ''
                k = 0
            elif i == ']':
                pre, n = sta.pop()
                cur = pre + (n*cur)
            else:
                cur += i
    
        return cur