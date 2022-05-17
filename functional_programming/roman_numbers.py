ROMAN_NUMBERS_BY_KEY = {
    1000:'M',
    900: 'CM',
    500: 'D',
    400: 'CD',
    100: 'C',
    90: 'XC',
    50: 'L',
    40: 'XL',
    10: 'X',
    9: 'IX',
    5: 'V',
    4: 'IV',
    1: 'I'
}

def numerals(num: int) -> str:

    result_value = ''
    for num_key in sorted(ROMAN_NUMBERS_BY_KEY.keys(), reverse=True):
        while num >= num_key:
            result_value += ROMAN_NUMBERS_BY_KEY[num_key]
            num -= num_key
    return result_value
