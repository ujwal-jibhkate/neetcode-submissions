class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_length = 0
        left = 0
        n = len(s)

        for right in range(n):
            # Shrink the window if a duplicate character is found
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length       