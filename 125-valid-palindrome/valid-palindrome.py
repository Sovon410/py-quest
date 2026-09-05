class Solution:
    def isAlphaNum(self, s: str) -> bool:
        if ('0' <= s <= '9') or ('a' <= s.lower() <= 'z'):
            return True
        return False   
     
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1
        while start < end:
            if not self.isAlphaNum(s[start]):
                start += 1
                continue
            if not self.isAlphaNum(s[end]):
                end -= 1
                continue
            if s[start].lower() != s[end].lower():
                return False
            
            start += 1
            end -= 1
        
        return True