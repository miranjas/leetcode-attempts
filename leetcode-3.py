class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substrings = {"":0, " ":1}
        sub = ""
        for i in s:
            if i in sub:
                substrings[sub] = len(sub)
                sub = ""
            sub += i
        return max(substrings.values())
                




x = Solution()
print(x.lengthOfLongestSubstring("abcabcbb"))
print(x.lengthOfLongestSubstring("bbbbb"))
print(x.lengthOfLongestSubstring("pwwkew"))
print(x.lengthOfLongestSubstring("pokemon"))
print(x.lengthOfLongestSubstring(""))
print(x.lengthOfLongestSubstring("_"))
