class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        com_pre = strs[0]
        for i in range(1, len(strs)):
            com_pre = self.find_pre(strs[i-1], strs[i], com_pre)
            # print(strs[i-1], strs[i], com_pre )
            if com_pre == "":
                return ""

        return com_pre

    def find_pre(self, str1: str, str2: str, pre: str) -> str:
        for i in range(min(len(str1), len(str2), len(pre))):
            if str1[i] != str2[i] or str2[i] != pre[i]:
                return pre[0:i]

        if len(str1) < len(str2): 
            if len(str1) < len(pre):
                return str1
            else:
                return pre

        else: 
            if len(str2) < len(pre):
                return str2
            else:
                return pre

