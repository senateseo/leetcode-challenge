class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        output=[]
        i=0

        while i < len(nums):
            st=i
            ptr=i
            while ptr < len(nums)-1 and nums[ptr]+1==nums[ptr+1]:
                ptr+=1
            ed=ptr
            if st!=ed:
                output.append('{st}->{ed}'.format(st=nums[st], ed=nums[ed]))
            else:
                output.append('{st}'.format(st=nums[st]))
            i=ptr+1
        return output
    
# TC : O(N)