def print_formatted(number):
    width = len(bin(number)) - 2

    for i in range(1, number+1):
        print(
            str(i).rjust(width, ' ').upper(),
            oct(i).replace('0o','').upper().rjust(width),
            hex(i).replace('0x','').upper().rjust(width),
            bin(i).replace('0b','').upper().rjust(width),
        )
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
