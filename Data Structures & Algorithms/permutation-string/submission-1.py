class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        if n > m:
            return False

        s1_fre = [0]*26
        

        for i in s1:
            s1_fre[ord(i)-97] += 1

        # for i in s2:
        #     s2_fre[ord(i)-97] += 1

        # print(s1_fre, s2_fre)

        s2_fre = [0]*26

        i = 0
        while i < n:
            s2_fre[ord(s2[i])-97] += 1
            i += 1
        if s1_fre == s2_fre:
            return True
        j = 0
        while i < m:
            print(i, j)
            if s2_fre == s1_fre:
                return True
            s2_fre[ord(s2[j])-97] -= 1
            s2_fre[ord(s2[i])-97] += 1
            i += 1
            j += 1
        if s1_fre == s2_fre:
            return True
        return False

        