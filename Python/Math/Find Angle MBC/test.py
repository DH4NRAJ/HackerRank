import math

if __name__ == "__main__":
    AB = int(input())
    BC = int(input())
    res = round(math.degrees(math.atan(AB/BC)))
    print(str(res)+'°')
