# Given a string s, find the length of the longest substring without repeating characters.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = {}
        start, max_length = 0, 0
        for end in range(len(s)):
            if s[end] in char_index_map:
                start = max(start, char_index_map[s[end]] + 1)
            char_index_map[s[end]] = end
            max_length = max(max_length, end - start + 1)
        return max_length