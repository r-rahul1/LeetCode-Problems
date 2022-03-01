class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        '''        
        arr={}
        t=""
        for i in range(max(indices)+1):
            arr[i]=s[indices.index(i)]

        return t.join(list(arr.values()))
        '''
        '''
        l = len(s)
        res = [None]*l
        for i in range(l):
            res[indices[i]]=s[i]
        return ''.join(res)
        '''
        
        res = [None]*len(s)
        
        for i in range(len(s)):
            res[indices[i]] = s[i]
        return ''.join(res)