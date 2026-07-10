class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += f"{i}\n"
        return res

    def decode(self, s: str) -> List[str]:
        print(s)
        return s.split("\n")[0:-1]