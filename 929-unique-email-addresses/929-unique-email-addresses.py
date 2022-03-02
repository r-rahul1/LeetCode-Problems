class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        dic = {}
        
        for email in emails:
            l,d = email.split("@")
            print(email,l,"->",d)
            temp = l.split("+")[0]
            
            t1 = "".join(temp.split("."))
            
            if t1+"@"+d not in dic:
                dic[t1+"@"+d] = 1

        return len(dic)