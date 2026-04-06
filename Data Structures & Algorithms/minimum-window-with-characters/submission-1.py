class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #have two map which will store need and current 
        # add each element to one and check with need if all valid or not
        #if valid return res 
        #check for window length if not valid remove left and check with need if greater than that or not
        # increase left and return res with substring of length

        need=Counter(t)
        window={}

        left = 0
        minlength = float('inf')
        res=""
        valid=0

        for right in range(len(s)):
            char = s[right]
            window[char] = 1+window.get(char,0)

            if char in need and window[char] == need[char]:
                valid+=1
            
            while valid == len(need):
                if right - left +1 < minlength:
                    minlength = right - left +1
                    res = s[left:right+1]

                window[s[left]]-=1

                if s[left] in need and window[s[left]] < need[s[left]]:
                    valid-=1
                left+=1
        return res
