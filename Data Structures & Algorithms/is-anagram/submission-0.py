class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        myMap = {}
        for i in range(len(s)):
            if s[i] not in myMap:
                myMap[s[i]] = 1
            else:
                myMap[s[i]] += 1
        for i in range(len(t)):
            if t[i] not in myMap:
                return False
            elif myMap[t[i]] <= 0:
                return False
            else: 
                myMap[t[i]] -= 1
        for i in myMap: 
            if myMap[i] != 0:
                return False
        return True 