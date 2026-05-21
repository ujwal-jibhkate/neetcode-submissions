class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Empty list for storing counter
        nums_dict ={}
        # create a counter dictionary
        for i in nums:
            if i not in nums_dict:
                nums_dict[i] = 1
            else:
                nums_dict[i] += 1

        # sort the dict with items as the key as sort key and in descending order
        sorted_items = sorted(nums_dict.items(), key=lambda x: x[1], reverse=True)

        # empty list for result to return
        result = []
        for i in range(k):
            result.append(sorted_items[i][0])

        return result