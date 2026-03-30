class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n

        def rev(nums,s,e):
            while s<e:
                nums[s],nums[e] = nums[e],nums[s]
                s+=1
                e-=1
        
        rev(nums,0,n-1)
        rev(nums,0,k-1)
        rev(nums,k,n-1)