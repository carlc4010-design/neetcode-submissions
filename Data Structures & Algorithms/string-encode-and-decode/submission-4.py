class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for c in strs:
            res.append(str(len(c))+"#"+c)
        return "".join(res)
    def decode(self, s: str) -> List[str]:
        count = 0
        res = []
        i = 0
        while i < len(s):
            if s[i] != "#":
                count = 10 * count + int(s[i])
                i += 1
            else:
                res.append(s[i+1:i+1 + count])
                i += count+1
                count = 0
        return res    