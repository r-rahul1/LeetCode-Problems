class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def fun(arr,rc):
            for x,y in rc:
                for i in range(len(matrix)):
                    arr[i][y] = 0
                for i in range(len(matrix[0])):
                    arr[x][i] = 0
                    
        rc = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rc.append((i,j)) 
        
        fun(matrix,rc)