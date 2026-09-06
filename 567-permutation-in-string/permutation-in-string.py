class Solution: 
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        freq = [0] * 26          # Initialize a list having 26 zeros.
        
        for i in range(len(s1)):
            freq[ord(s1[i]) - ord("a")] += 1
        
        windo_size = len(s1)
        
        for i in range(len(s2)):
            windo_index, idx = 0, i
            windo_freq = [0] * 26
            
            while windo_index < windo_size and idx < len(s2):
                windo_freq[ord(s2[idx]) - ord("a")] += 1
                windo_index += 1
                idx += 1
            
            if freq == windo_freq:
                return True
            
        return False