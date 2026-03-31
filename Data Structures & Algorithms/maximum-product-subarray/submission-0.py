class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi = nums[0]
        mini = nums[0]
        ans = nums[0]

        for i in range(1,len(nums)):
            n = nums[i]
            temp = maxi
            maxi = max(n,temp*n,mini*n)
            mini = min(n,temp*n,mini*n)

            ans = max(maxi,ans)
        return ans