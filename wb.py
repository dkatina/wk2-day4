

def check_letter(a, b):
    if a.isalpha() and b.isalpha():
        if a > 'Z' and b > 'Z':
            return 1
        elif a <= 'Z' and b <= 'Z':
            return 1
        else:
            return 0
    else: 
        return -1
    
print(check_letter(':','b'))

def check_letter2(a,b):
    up_key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    low_key = 'abcdefghijklmnopqrstuvwxyz'
    if a in up_key or a in low_key:
        if b in up_key or b in low_key:
            if a in up_key and b in up_key:
                return 1
            elif a in low_key and b in low_key:
                return 1
            else:
                return 0
    return -1
        