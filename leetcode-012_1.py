class Solution:
    def intToRoman(self, num: int) -> str:
        result = ''
        if num >= 1000:
            M_num = num // 1000
            result += 'M' * M_num
            num %= 1000
        if num >= 100:
            if num // 100 == 9:
                result += 'CM'
            elif num >= 500:
                result += 'D'
                C_num = (num - 500) // 100
                result += 'C' * C_num
            elif num // 100 == 4:
                result += 'CD'
            else:
                C_num = num // 100
                result += 'C' * C_num
            num %= 100
        if num >= 10:
            if num // 10 == 9:
                result += 'XC'
            elif num >= 50:
                result += 'L'
                X_num = (num - 50) // 10
                result += 'X' * X_num
            elif num // 10 == 4:
                result += 'XL'
            else:
                X_num = num // 10
                result += 'X' * X_num
            num %= 10
        if num == 9:
            result += 'IX'
        elif num >= 5:
            result += 'V'
            I_num = num - 5
            result += 'I' * I_num
        elif num == 4:
            result += 'IV'
        else:
            result += 'I' * num
        return result