class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        res = -1
        for i, val in enumerate (nums):

            if target <= val:
                return i
        return len(nums)
