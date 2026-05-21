class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_arr = set(nums)

        if len(nums_arr) == len(nums):
            return False
        else:
            return True

