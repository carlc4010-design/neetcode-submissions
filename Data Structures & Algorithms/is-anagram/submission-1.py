class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = [0]*26
        if len(s) != len(t):
            return False
        
        for c in s:
            map[ord(c)-ord("a")] += 1
        for c in t:
            map[ord(c)-ord("a")] -= 1
        for i in range(len(map)):
            if map[i] != 0:
                return False
        return True