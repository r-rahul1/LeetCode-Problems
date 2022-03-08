class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rz = False
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i > 0:
                        matrix[i][0] = 0
                    else:
                        rz = True
                    matrix[0][j] = 0
                    
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for i in range(len(matrix)):
                matrix[i][0] = 0  
            
        if rz:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
                           
        
        '''
        #Space complexity -> O(m+n)
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
        '''