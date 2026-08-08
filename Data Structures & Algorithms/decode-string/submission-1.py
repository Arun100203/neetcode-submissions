class Solution:
    def decodeString(self, s: str) -> str:
        sta = []
        m = len(s)
        for i in range(m):
            if s[i] ==']':
                t = ""
                while sta and sta[-1] != '[':
                    t = sta[-1] + t
                    sta.pop()
                sta.pop()
                print(t)
                n = ''
                while sta and sta[-1] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                    n = sta[-1] + n
                    sta.pop()
                print(n)
                t = t * int(n)
                sta.append(t)
                print(t)
                # print(res)
                
            else:
                sta.append(s[i])

            print(sta)

        return "".join(sta)