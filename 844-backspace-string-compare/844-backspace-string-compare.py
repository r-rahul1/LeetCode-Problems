class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        t1 = []
        t2 = []
        
        def fun(temp,st):
            for i in st:
                if  i == '#':
                    if temp:
                        temp.pop()
                else:
                    temp.append(i)
        
        fun(t1,s)
        fun(t2,t)
        print(t1,t2)
        return True if t1==t2 else False