class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.dic = {x:[None,[]] for x in range(len(parent))}
        self.dic[0] = [None,[]]
        #self.count = 0
        for x in range(1,len(parent)):
            self.dic[parent[x]][1].append(x)

    def lock(self, num: int, user: int) -> bool:
        if self.dic[num][0]:
            return False
        self.dic[num][0] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if not self.dic[num][0] or self.dic[num][0] != user:
            return False
        self.dic[num][0] = None
        return True

    def upgrade(self, num: int, user: int) -> bool:
        
        def check():
            #checking ancestors
            acending = self.parent[num]
            while acending != -1:
                if self.dic[acending][0]:
                    return False
                acending = self.parent[acending]
            
            self.count = 0
            #checking and unlocking decendants

            def fun(temp):
                for x in self.dic[temp][1]:
                    if self.dic[x][0]:
                        self.count += 1
                        self.dic[x][0] = None
                    fun(x)
            fun(num)        
            return True if self.count != 0 else False
                
        if self.dic[num][0] or not check():
            return False        
        
        self.dic[num][0] = user
        return True

# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)