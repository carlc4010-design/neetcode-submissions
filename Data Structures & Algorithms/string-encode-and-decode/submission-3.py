class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for c in strs:
            res += str(len(c)) + "#" + c
        return res
    def decode(self, s: str) -> List[str]:
        count = 0
        content = False
        res = ""
        myStr = []
        for c in s:
            if content == False and c != "#":
                count = count * 10 + int(c)
                continue
            elif content == False and c == "#":
                
                if count == 0:
                    myStr.append("")
                else:
                    content = True
                continue
            
            res += c
            count -= 1
            if count == 0:
                content = False
                myStr.append(res)
                res = ""
        return myStr
