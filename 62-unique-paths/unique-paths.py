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



        