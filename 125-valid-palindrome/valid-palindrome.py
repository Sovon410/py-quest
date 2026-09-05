class Solution:
    def isAlphaNum(self, s: str) -> bool:
        if (s >= '0' and s <= '9') or (s >= 'a' and s <= 'z'):
            return True
        return False   
     
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        start, end = 0, len(s) - 1
        while start < end:
            if not self.isAlphaNum(s[start]):
                start += 1
                continue
            if not self.isAlphaNum(s[end]):
                end -= 1
                continue
            if s[start] != s[end]:
                return False
            
            start += 1
            end -= 1
        
        return True