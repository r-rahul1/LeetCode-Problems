class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left,right = 0,len(matrix[0])
        top,bottom = 0,len(matrix)
        
        while left < right and top < bottom:
            
            for i in range(left,right):
                res.append(matrix[top][i])
            top += 1
            
            for i in range(top,bottom):
                res.append(matrix[i][right-1])
            right -= 1
            
            if not (left < right and top < bottom):
                break
            
            for i in range(right-1,left-1,-1):
                res.append(matrix[bottom-1][i])
            bottom -= 1
            
            for i in range(bottom-1,top-1,-1):
                res.append(matrix[i][left])
            left += 1
            
        return res        
        
        #recursion method
        '''
        res = []
        def fun(nums,top,left,right,bottom):
            if top >= bottom or left >= right:
                return
            
            for i in range(left,right):
                res.append(nums[top][i])
            top += 1
            
            for i in range(top,bottom):
                res.append(nums[i][right-1])
            right -= 1
            
            if not (left < right and bottom > top):
                return
            
            for i in range(right-1,left-1,-1):
                res.append(nums[bottom-1][i])
            bottom -=1
            
            for i in range(bottom-1,top-1,-1):
                res.append(nums[i][left])
            left += 1
            
            fun(nums,top,left,right,bottom)
            
        fun(matrix,0,0,len(matrix[0]),len(matrix))
        return res
        '''
