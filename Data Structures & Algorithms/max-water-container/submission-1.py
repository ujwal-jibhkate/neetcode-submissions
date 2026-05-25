class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # to save the result
        result = 0

        # right and left pointers
        l = 0
        r = len(heights) - 1

        while l < r:
            # calculate area
            area = (r - l) * min(heights[r], heights[l])
            # save the larger one
            result = max(result, area)

            # update the pointers depending upon the 
            # larger height
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        # return result
        return result