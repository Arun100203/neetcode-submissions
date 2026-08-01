class Solution:
    def isValid(self, s: str) -> bool:
        res=[]
        n=len(s)
        not_matched = []
        for i in range(n):
            i = s[i]
            print(res)
            if i == '{' or i== '[' or i== '(':
                res.append(i)
            else:
                if i == '}' and res and res[-1] == '{':
                    res.pop()
                elif  i == ')' and res and res[-1] == '(':
                    res.pop()
                elif  i == ']' and res and res[-1] == '[':
                    res.pop()
                else:
                    not_matched.append(i)

        return len(res) == 0 and len(not_matched) == 0