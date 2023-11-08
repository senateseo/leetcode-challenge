class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # rough approach
        # Count every elements' occurences and choose the answer which is greater than n/2 times.
        # But above approach takes more than O(1) space (actually, it takes O(n)).

        cnt=0
        candidate = 0

        for num in nums:
            if cnt==0:
                candidate = num
            if num==candidate:
                cnt+=1
            else:
                cnt-=1

        return candidate

        
        
        # O(n) Time complexity
        # O(1) Space