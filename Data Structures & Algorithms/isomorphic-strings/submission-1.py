class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        a={}
        b={}

        for i in range(len(s)):
            c1 = s[i]
            c2 =t[i]

            if c1 in a:
                if a[c1]!=c2:
                    return False
            else:
                a[c1] = c2
            
            if c2 in b:
                if b[c2]!=c1:
                    return False
            else:
                b[c2] = c1
            
        return True