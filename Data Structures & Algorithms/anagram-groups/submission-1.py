class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # To store all the results anagrams to return
        anagrams = []

        # to track the seen indices
        seen_indices = set()

        # 1st loop over the entire list of strs
        for i in range(len(strs)):
            # if this index already exist, then skip
            if i in seen_indices:
                continue

            # look at current individual str
            current_str = strs[i]
            # to check if our current str has anagrams
            anagrams_for_cur = []    # first internal empty list for this one
            anagrams_for_cur.append(current_str) # append itself first
            seen_indices.add(i)  # add this index to seen indices

            # now from next index over entire remaining strs
            for j in range(i + 1, len(strs)):
                next_str = strs[j] # check for each other str in strs
                if len(current_str) != len(next_str):
                    continue
                elif sorted(current_str) == sorted(next_str):
                    anagrams_for_cur.append(next_str)
                    seen_indices.add(j)

            # append entire anagrams list
            anagrams.append(anagrams_for_cur)

        return anagrams
