def ator(number):
    convert = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'],[ 100, 'C'], [ 90, 'XC'], [ 50, 'L'], [ 40, 'XL'],[  10, 'X'], [  9, 'IX'], [  5, 'V'], [  4, 'IV'],[   1, 'I']]
    result = ''
    for denominator, roman_digit in convert:
        result += roman_digit*(number/denominator)
        number %= denominator
    return result
def rtoa(number):
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(number)):
        if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
            result += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
        else:
            result += rom_val[s[i]]
    return result

print(ator(input('Insert arabic number here :')))
print(rtoa(input('Insert roman number here :')))