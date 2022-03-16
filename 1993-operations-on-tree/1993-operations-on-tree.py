class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.dic = {}
        self.children = {}
        self.dic[0] = [None,0]
        for x in range(1,len(parent)):
            self.dic[x] = [None,0]
            if x not in self.children:
                self.children[x] = []
            if parent[x] in self.children:
                self.children[parent[x]].append(x)
            else:
                self.children[parent[x]] = [x]

    def lock(self, num: int, user: int) -> bool:
        if self.dic[num][0]:
            return False
        
        self.dic[num][0] = user
        acending = self.parent[num]
        while acending != -1:
            self.dic[acending][1] += 1
            acending = self.parent[acending]
        
        return True
    
    def unlock(self, num: int, user: int) -> bool:
        if not self.dic[num][0] or self.dic[num][0] != user:
            return False
        
        self.dic[num][0] = None
        acending = self.parent[num]
        while acending != -1:
            self.dic[acending][1] -= 1
            acending = self.parent[acending]
        
        return True

    def upgrade(self, num: int, user: int) -> bool:
        
        def check(num):
            #checking ancestors
            acending = self.parent[num]
            while acending != -1:
                if self.dic[acending][0]:
                    return False
                acending = self.parent[acending]
            
            #checking and unlocking decendants
            def fun(temp):
                for x in self.children[temp]:
                    self.dic[x][1] = 0
                    self.dic[x][0] = None
                    if self.children[x]:
                        fun(x)
                    
            fun(num)        
            return True
                
        if self.dic[num][0] or self.dic[num][1] == 0 or not check(num):
            return False        
        
        self.dic[num][1] = 0
        self.dic[num][0] = user
        return True

# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)