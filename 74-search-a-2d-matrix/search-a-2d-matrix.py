class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])

        low = 0
        high = (r*c) - 1


        while low <= high:

            mid = (high + low) // 2

            if target == matrix[mid//c][mid%c]:
                return True
            
            elif target > matrix[mid//c][mid%c]:
                low  = mid + 1
            
            elif target <  matrix[mid//c][mid%c]:
                high = mid - 1
        
        return False

        