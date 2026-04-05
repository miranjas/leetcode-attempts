class Solution:
    def reverse(self, x: int) -> int:
        # handle positive numbers
        if x > 0:
            x = str(x)[::-1]
            x = int(x)
        # handle negative numbers
        if x < 0:
            x = str(x)[1:]
            x = x[::-1]
            x = int(x)
            x = x * -1
        # check if the reversed number is within the 32-bit signed integer range
        if x > int(2**31 -1):
            return 0
        if x < int(2**31 * -1):
            return 0
        return x

            