class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # iterate through the digits in reverse order
        for i in range(len(digits) - 1, -1, -1):
            # if the current digit is less than 9, we can simply add 1 and return the result
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                # otherwise, we need to set the current digit to 0 and continue to the next digit
                digits[i] = 0
        # if we make it to here then all the digits were 9, so we need to add a new digit at the beginning of the list
        return [1] + digits
            


solution = Solution()
print(solution.plusOne([1, 2, 3]))
print(solution.plusOne([4, 3, 2, 1]))
print(solution.plusOne([9]))