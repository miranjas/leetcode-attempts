class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # create 2 varaibles to contain left pointer and max length
        l, max_length = 0,0
        # initialize unique character set we will use as sliding window view of characters in s
        char_set = set()

        # we iterate over the string characters up to the right pointer - current substring
        for r in range(len(s)):
            # checking for repeateed characters
            while s[r] in char_set:
                # this will be triggered when encountering a repeat character that's already in set
                # we remove characters from set and adjust left pointer until the repeat is no longer in set
                char_set.remove(s[l])
                l +=1
            # if while statement is not trigerred, we can add character to the set
            char_set.add(s[r])
            # this line below compares the current max_value against the current length of substring
            # the higher value becomes the new max_value length
            max_length = max(max_length, r-l + 1)
        return max_length



x = Solution()
print(x.lengthOfLongestSubstring("abcabcbb"))
print(x.lengthOfLongestSubstring("bbbbb"))
print(x.lengthOfLongestSubstring("pwwkew"))
print(x.lengthOfLongestSubstring("pokemon"))
print(x.lengthOfLongestSubstring(""))
print(x.lengthOfLongestSubstring("_"))
