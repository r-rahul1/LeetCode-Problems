class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) > m*n or len(original) < m*n:
            return []
        res = [[None for i in range(n)] for j in range(m)]
        i,j = 0,0
        for num in original:
            if j == n:
                j = 0
                i += 1
            res[i][j] = num
            j += 1
        
        return res