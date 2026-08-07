class Solution:
    def simplifyPath(self, path: str) -> str:
        sta = path.split("/")
        res = []
        for i in sta:
            if i == "" or i == '.':
                continue
            elif i == ".." :
                if res:
                    res.pop()
            else:
                res.append(i)


        # print(res)
        
        return  "/" +"/".join(res)
         