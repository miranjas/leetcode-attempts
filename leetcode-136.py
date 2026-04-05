class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        seen = {}
        # keeping track of how many times each number appears in the list
        for i in nums:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        # getting the number that appears once
        single = min(seen.values())
        # finding the key for the value that appears once
        for key in seen:
            if seen[key] == single:
                return key



solution = Solution()
print(solution.singleNumber([2,2,1]))
print(solution.singleNumber([4,1,2,1,2]))
print(solution.singleNumber([1]))