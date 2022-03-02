class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        
        for email in emails:
            l,d = email.split("@")
            t1 = l.split("+")[0].replace(".","")
            res.add(t1+"@"+d)

        return len(res)