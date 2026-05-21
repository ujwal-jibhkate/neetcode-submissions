class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_arr = set()

        for i in nums:
            if i not in nums_arr:
                nums_arr.add(i)
            else:
                return True

        return False