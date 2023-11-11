# Approach 2: Iterative
# TC: O(N)
# SC: O(1)


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        if len(nums)==1:
            return True

        pos=0
        jumps=nums[pos]

        while jumps>0:
            if pos+jumps >= len(nums)-1:
                return True
            pos+=1
            if nums[pos] >= jumps:
                jumps = nums[pos]
            else:
                jumps-=1
    
        return False


        # Edge case : The number of elements is 1 => True





# Approach 2: Recursive
# TC: O(N)
# SC: O(N)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        return self.canReach(nums, 0, len(nums)-1)
        
    def canReach(self, nums, start, end):
        if start==end:
            return True
        
        for i in range(end-1, start-1, -1):
            dist = end-i
            if dist <= nums[i]:
                return self.canReach(nums, start, i)
        return False