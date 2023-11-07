class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        ctn=0
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                if ctn<2:
                    nums[k]=nums[i]
                    k+=1
                ctn+=1
            else:
                if ctn<2:
                    nums[k]=nums[i]
                    k+=1
                ctn=0
        
        if ctn<2:
            nums[k]=nums[-1]
            k+=1
        return k
        
# 1. The key point is comparing elements to backwards rather than forwards.
# 2. The key point is using the hint (non-decreasing elements) 