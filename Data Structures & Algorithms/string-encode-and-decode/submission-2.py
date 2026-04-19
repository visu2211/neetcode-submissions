class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += s + "(a**a)"
        return res

    def decode(self, s: str) -> List[str]:
        return s.split("(a**a)")[:-1]