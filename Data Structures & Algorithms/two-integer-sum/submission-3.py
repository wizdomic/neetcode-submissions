class Solution:
    def twoSum(self, nums: List[int], target:int)-> List[int]:
        sett={}
        for i,num in enumerate(nums):
            if target-num in sett:
                return [sett[target-num],i]
            sett[num]=i
        return []