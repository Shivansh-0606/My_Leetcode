class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def F(i,j):
            if i == 0 and j == 0:
                return 1
            
            if i < 0 or j < 0:
                return 0
            
            left = F(i-1,j)
            up = F(i , j-1)

            return left + up
        
        
        return F(m-1,n-1)