class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max=nums[0]
        cur_min=nums[0]
        res=nums[0]

        for i in range(1,len(nums)):
            n=nums[i]

            temp = cur_max
            cur_max = max(n,n*temp,n*cur_min)
            cur_min = min(n,n*temp,n*cur_min)

            res=max(res,cur_max)
        return res