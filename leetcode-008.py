class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        if str == '':
            return 0
        result = ''
        if not str.startswith(('+', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9')):
            return 0
        else:
            result += str[0]
            str = str[1:]
        while str.startswith(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')):
            result += str[0]
            str = str[1:]
        try:
            result = int(result)
        except:
            return 0
        if result < -2147483648:
            return -2147483648
        if result > 2147483647:
            return 2147483647
        return result