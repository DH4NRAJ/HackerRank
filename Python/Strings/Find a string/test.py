def count_substring(string, sub_string):
    count = 0
    start = 0
    while start < len(string):
        flag = string.find(sub_string,start)
        if flag != -1:
            start = flag+1
            count += 1
        else:
            return count
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
