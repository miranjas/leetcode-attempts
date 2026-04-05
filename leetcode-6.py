class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= numRows or numRows == 1:
            return s
        # defining cycle length for zigzag pattern
        cycle = numRows * 2 - 2
        new = ""
        for i in range(numRows):
            # for each row, we iterage in steps of cycle length
            for j in range(i, len(s), cycle):
                new += s[j]
                # handling middle characters in zigzag, out of bounds check is needed
                if i != 0 and i != numRows -1 and j + cycle - 2 * i < len(s):
                    new += s[j + cycle -2 * i]
        return new

solution = Solution()
print(solution.convert("PAYPALISHIRING", 3))
print(solution.convert("PAYPALISHIRING", 4))
print(solution.convert("A", 1))

        
            
