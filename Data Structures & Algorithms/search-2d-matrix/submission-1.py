class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while l <= r:
            m = (l + r) // 2
            left, right = 0, len(matrix[m]) - 1
            
            while left <= right:
                mid = (left + right) // 2

                if target < matrix[m][left]:
                    r = m - 1
                    break
                    
                if target > matrix[m][right]:
                    l = m + 1
                    break

                if target > matrix[m][mid]:
                    left = mid + 1
                elif target < matrix[m][mid]:
                    right = mid - 1
                else:
                    return True
        
        return False


