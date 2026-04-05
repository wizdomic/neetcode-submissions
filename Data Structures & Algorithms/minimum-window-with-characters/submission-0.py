class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = {}

        l = 0
        valid=0
        minlen = float('inf')
        res = ""

        for r in range(len(s)):
            char = s[r]
            
            window[char] = 1 + window.get(char,0)

            if char in need and window[char] == need[char]:
                valid+=1
            
            while valid == len(need):
                if r - l + 1 < minlen:
                    minlen = r-l+1
                    res = s[l:r+1]
                
                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    valid-=1
                l+=1
        return res