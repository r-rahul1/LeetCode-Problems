class Solution:
    def simplifyPath(self, path: str) -> str:
        temp = path.split('/')
        res = []
        for s in temp:
            if s:
                if s == '..':
                    if res:
                        res.pop()
                elif s != '.':
                    res.append(s)    

        return '/'+'/'.join(res) if res else '/'