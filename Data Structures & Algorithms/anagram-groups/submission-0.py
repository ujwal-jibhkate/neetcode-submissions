class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        seen_indices = set()
        for i in range(len(strs)):
            if i in seen_indices:
                continue
            current_str = strs[i]
            anagrams_for_cur = []    
            anagrams_for_cur.append(current_str)
            seen_indices.add(i)
            for j in range(i + 1, len(strs)):
                next_str = strs[j]
                if len(current_str) != len(next_str):
                    continue
                elif sorted(current_str) == sorted(next_str):
                    anagrams_for_cur.append(next_str)
                    seen_indices.add(j)

            anagrams.append(anagrams_for_cur)

        return anagrams
