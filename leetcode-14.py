class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""
        # setting shortest word from strs
        # anything longer cant count as a common prefix
        shortest = min(strs,key=len)
        if len(strs) == 0:
            return prefix
        
        # iterating through letters in shortest word and comparing to the same index in all other words
        for i in range(len(shortest)):
            for words in strs:
                # if different letter at the index, return what we have
                if shortest[i] != words[i]:
                    return prefix
            prefix += words[i]
        return prefix

