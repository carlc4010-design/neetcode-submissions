class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for c in strs:
            res +=  c+"好" 
        return res

    def decode(self, s: str) -> List[str]:
        strs = []
        res = ""
        for c in s:
          
            if c != "好":
               res+= c
            else:
                strs.append(res)
                res = ""
        return strs