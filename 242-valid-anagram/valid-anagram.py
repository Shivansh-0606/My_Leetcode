class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counts = [0] * 26

        for char_s  , char_t in zip(s,t):
            counts[ord(char_s) - ord('a')]+=1
            counts[ord(char_t) - ord('a')]-=1
        
        return all(c == 0 for c in counts)