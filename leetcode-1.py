class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # start by creating a hashmap where we'll store seen values and their indices
        # this also makes our solution O(1)
        seen = {}
        # using range(len()) lets us work with the indexes of the list rather than direct values
        # this makes it easier to narrow down the indices to our solution
        for index in range(len(nums)):
            num = nums[index] # current number
            remainder = target - num # the value we need to reach the target
            
            # checking if the remainder has been in seen already, if so return it
            # if not we can store the current number with its index until we find the correct pair
            if remainder in seen:
                return [seen[remainder], index]
            seen[num] = index





x = Solution()
print(x.twoSum([11,5,35,44,22,66,77],33))

# edge cases to consider (duplicates, no answer,zeros, negatives)
print(x.twoSum([5,5],10))
print(x.twoSum([5,6],10))
print(x.twoSum([0,5,5],10))
print(x.twoSum([-5,15],10))

