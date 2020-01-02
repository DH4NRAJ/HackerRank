if __name__ == '__main__':
    n = int(input())
    marks_sheet = [[input(),float(input())]for _ in range(n)]
    second = sorted(list(set([marks for name,marks in marks_sheet])))[1]
    print('\n'.join([a for a,b in sorted(marks_sheet) if b == second]))
