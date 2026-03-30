class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged=[]

        for interval in intervals:
            if not merged:
                merged.append(interval)
            else:
                prev = merged[-1]

                if prev[1] < interval[0]:
                    merged.append(interval)
                else:
                    prev[-1] = max(prev[1],interval[1])
        return merged