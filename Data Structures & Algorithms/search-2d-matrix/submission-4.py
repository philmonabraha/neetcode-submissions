class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row = len(matrix)
        col = len(matrix[0])
        left, right = 0, ((row * col)-1)

        while left <= right:

            mid = left + (right - left)//2
            i = (mid // col) - 1
            j = (mid % col) -1

            if target == matrix[i][j]:
                return True
            elif target > matrix[i][j]:
                left = mid + 1
            else:
                right = mid - 1

        return False


        