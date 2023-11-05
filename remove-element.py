class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # [0, 1, 2, 2, 3, 0, 4, 2]

        k=0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k]=nums[i]
                k+=1
        return k


# ...
# ignore rest of the space, you can just overwrite it.