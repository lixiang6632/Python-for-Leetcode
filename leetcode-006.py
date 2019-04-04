class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        result = [''] * (numRows+1)
        curRow, direction = 1, 1
        for ch in s:
            result[curRow] += ch
            if (direction > 0 and curRow == numRows) or (direction < 0 and curRow == 1):
                direction *= -1
            curRow += direction
        final_result = ''
        for row in range(1, numRows + 1):
            final_result += result[row]
        return final_result