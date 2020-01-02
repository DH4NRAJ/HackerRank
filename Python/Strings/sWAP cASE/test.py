def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
    
"""
#A bit bigger code
def swap_case(s):
    result =""
    for x in s:
        if (x.islower()):
            result += x.upper()
        elif (x.isupper()):
            result += x.lower()
        else:
            result += x
    return result
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
"""
