class Solution:
    def isan(self,x):
        if ord("A") <= ord(x) <= ord("Z"):
            return True
        if ord("a") <= ord(x) <= ord("z"):
            return True
        if ord("0") <= ord(x) <= ord("0"):
            return True
        return False
    def isPalindrome(self, s: str) -> bool:
        myStr = "".join(c for c in s if c.isalnum())
        myStr = myStr.lower()
        left = 0
        right = len(myStr) - 1
        while right >= left:
            if myStr[left] != myStr[right]:
                return False
            else:
                left  +=  1
                right -=  1
        return True
        