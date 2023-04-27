def clamp(x, lo, hi):
    return min(max(x, lo), hi)

def atoi(s):
    s = s.strip()
    
    if len(s) == 0:
        return 0

    read_sign = False
    read_number = False
    in_number = False

    num = ""
    for char in s:
        print(num)
        if char in ['-', '+'] and not read_sign and not read_number and not in_number:
            if char == '-':
                num += char
            read_sign = True
            continue

        if char.isnumeric():
            num += char
            in_number = True
        
        if in_number and not char.isnumeric():
            in_number = False
            read_number = True
        
        if read_number and not char.isnumeric():
            break
        
        if not char.isnumeric() and (not read_number or not in_number):
            return 0
    
    print(num)
    if num.lstrip('-').isnumeric():
        return clamp(int(num), -2**31, 2**31 - 1)
    else:
        return 0

class Solution:
    def myAtoi(self, s: str) -> int:
        return atoi(s)
            
