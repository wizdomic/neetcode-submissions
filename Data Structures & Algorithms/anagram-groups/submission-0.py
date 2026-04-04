class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for c in strs:
            key = "".join(sorted(c)) #act cat=act
            
            if key not in res:
                res[key] = []
            
            res[key].append(c)
        
        return list(res.values())