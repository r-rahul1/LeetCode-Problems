class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        for i in range(n+1):
            temp=(bin(i).replace("0b",""))
            res.append(temp.count('1'))
        return res