class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        # Minimum Kitni bar repeat krna hoga
        k = ((len(b) + len(a) - 1) // len(a))

        if b in (a * k):
            return k
        if b in (a * (k+1)):
            return k+1
        
        return -1