# Given a string s, return the longest palindromic substring in s.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        for i in range(0, len(s)):
            if i == 0:
                if s == s[::-1]:
                    return s
            elif s[i:] == s[i:][::-1] or s[:-i] == s[:-i][::-1]:
                return s[i:] if s[i:] == s[i:][::-1] else s[:-i]
            elif s[i:-i] == s[i:-i][::-1]:
                return s[i:-i]
