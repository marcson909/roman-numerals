from roman_numerals import to_roman
from roman_numerals import to_roman_modern


# lazy test cases
print(to_roman(1) == 'I')
print(to_roman(3) == 'III')
print(to_roman(4) == 'IIII')
print(to_roman(300) == 'CCC')
print(to_roman(123) == 'CXXIII')
print(to_roman(2400) == 'MMCCCC')
print(to_roman(939) == 'DCCCCXXXVIIII')

# modern test cases
print(to_roman_modern(1) == 'I')
print(to_roman_modern(3) == 'III')
print(to_roman_modern(4) == 'IV')
print(to_roman_modern(300) == 'CCC')
print(to_roman_modern(123) =='CXXIII')
print(to_roman_modern(2400) == 'MMCD')
print(to_roman_modern(939) == 'CMXXXIX')
print(to_roman_modern(594) == 'DXCIV')