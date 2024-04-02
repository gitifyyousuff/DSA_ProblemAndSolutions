class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows = len(matrix)
        cols = len(matrix[0])

        #to find specific row our target might present
        top = 0
        bottom = rows-1

        while top <= bottom:
            row_val = (top+bottom)//2

            if target>matrix[row_val][-1]:
                top = row_val+1
            elif target < matrix[row_val][0]:
                bottom = row_val -1
            else:
                break


        if top>bottom:
            return False

        
        #chck specific row whether target value present or not

        left =0
        right = cols-1
        row_target = (top+bottom)//2

        while left<=right:
            mid = (left+right)//2
            if target >matrix[row_target][mid]:
                left = mid+1
            elif target < matrix[row_target][mid]:
                right = mid-1
            else:
                return True

        return False









        