class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, (rows * cols) - 1

        while low <= high:
            mid = (low + high) // 2
            midRow = mid // cols
            midCol = mid % cols

            current = matrix[midRow][midCol]
            if current == target:
                return True
            elif current > target:
                high = mid - 1
            else:
                low = mid + 1
        
        return False