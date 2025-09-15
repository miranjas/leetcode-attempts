class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if the length of both strings isnt the same, we know it cant be true
        if len(s) != len(t):
            return False 
        
        # otherwise we can keep track of the letters and their frequencies in both words
        # using a dictionary for both words and iterating through each letter
        characters_s = {}
        characters_t = {}
        for char in s:
            if char in characters_s:
                characters_s[char] += 1
            else:
                characters_s[char] = 1

        for char in t:
            if char in characters_t:
                characters_t[char] += 1
            else:
                characters_t[char] = 1
        
        # once we find the letters and frequencies of both s and t, we can compare the dictionaries for equivalency
        if characters_s == characters_t:
            return True
        else:
            return False

