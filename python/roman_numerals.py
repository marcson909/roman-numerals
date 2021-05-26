roman_dict= {
    1000: "M",
    500: "D",
    100: "C",
    50: "L",
    10: "X",
    5: "V",
    1: "I"
    }

roman_dict_modern = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I"
    }
def to_roman(num):
    return convert_to_roman(num, roman_dict)

def to_roman_modern(num):
    return convert_to_roman(num, roman_dict_modern)



def convert_to_roman(num, conversion_dict):
    # write your code here!
    answer = ""
    
    
    for x in conversion_dict:
        
        result = num // x
        
        for i in range(result):
            answer += conversion_dict[x]
        
        num = num % x
        
        if num == 0:
            break
    return answer

print(to_roman(444))
print(to_roman_modern(444))
        
