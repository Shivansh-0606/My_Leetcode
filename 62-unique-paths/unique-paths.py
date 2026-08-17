Using Tabulation:-
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0]*n for _ in range(m)]
       
        for i in range(m):
            for j in range(n):
      
                if i == 0 and j == 0:
                    dp[i][j] = 1
                else:
                    left = 0
                    up = 0
                    
                    if i > 0:
                        up = dp[i-1][j]
                    if j > 0:    
                        left = dp[i][j-1]
                    
                    dp[i][j] = up + left
        
        return dp[m-1][n-1]

using Memoizaion:-
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[-1] * n for _ in range(m)]

        def calculate_path(i:int , j:int) -> int:
            if i == 0 and j == 0:
                return 1
            if i < 0 or j < 0:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            dp[i][j] = calculate_path(i-1,j) + calculate_path(i , j -1)

            return dp[i][j]
        
        return calculate_path(m-1,n-1)

Using Recurison:-
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

        
