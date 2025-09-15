class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # since sets cannot contain duplicates, we can convert
        # nums into a set and compare it's length to the original array
        # sets will get rid of duplicates when converting which is why this works
        if len(set(nums)) == len(nums):
            return False
        return True
    
# alternatively, we can iterate through nums and add each index to our seen set
# we can have an if statement to verify if the current index is in the set or not before adding
'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
'''