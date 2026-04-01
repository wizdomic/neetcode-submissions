class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        m = 0 

        while(l<r):
            h = min(heights[l],heights[r])
            w = r-l
            m = max (m,h*w)

            if l<r and heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return m