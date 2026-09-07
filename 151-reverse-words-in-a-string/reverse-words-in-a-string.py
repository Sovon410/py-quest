class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ""
        i = 0
        n = len(s)
        
        while i < n:
            # 1. Skip any leading or multiple spaces
            while i < n and s[i] == " ":
                i += 1
            
            # If we reached the end of the string, break out
            # if i >= n:
            #     break
                
            # 2. Extract the current word
            word = ""
            while i < n and s[i] != " ":
                word += s[i]
                i += 1
            
            # 3. Prepend the word to our final answer
            if word != "":
                if ans == "":
                    ans = word
                else:
                    ans = word + " " + ans
                
        return ans