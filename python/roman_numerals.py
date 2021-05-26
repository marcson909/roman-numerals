def to_roman(num):
    # write your code here!
    answer = ""
    roman_dict = {
    1000: "M",
    500: "D",
    100: "C",
    50: "L",
    10: "X",
    5: "V",
    1: "I"
    }
    
    for x in roman_dict:
        
        result = num // x
        
        for i in range(result):
            answer += roman_dict[x]
        
        num = num % x
        
        if num == 0:
            break
    return answer

print(to_roman(14))
        
