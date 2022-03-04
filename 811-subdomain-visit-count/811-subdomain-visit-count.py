class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic = collections.Counter()
        
        for cpd in cpdomains:
            freq,domain = cpd.split()
            
            freq = int(freq)
            temp = domain.split('.')
            for i in range(len(temp)):
                dic['.'.join(temp[i:])] += freq
        
        return ["{} {}".format(freq,domain) for domain,freq in dic.items()]
        