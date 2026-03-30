class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = nums[0]
        answer = nums[0]

        for i in range(1, len(nums)):
            cur_sum = max(nums[i], cur_sum + nums[i])
            answer = max(answer, cur_sum)

        return answer