class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_product  = []
        length = len(nums)

        if length == 2:
            return nums[::-1]

        for i in range(length):
            product = 1
            for j in range(length):
                if i != j :
                    product = product * nums[j]

            nums_product.append(product)

        return nums_product


        