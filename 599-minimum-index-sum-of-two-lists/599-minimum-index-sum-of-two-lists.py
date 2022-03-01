import math
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic = {}
        
        for i,item in enumerate(list1):
            dic[item] = i
        
        res,avg = None,math.inf
        ans = []
        for i,item in enumerate(list2):
            if item in dic:
                if i+dic[item] < avg:
                    avg = i+dic[item]
                    ans = [item]
                elif i+dic[item] == avg:
                    ans.append(item)
                

        return ans
        