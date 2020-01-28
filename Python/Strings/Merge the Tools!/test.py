def merge_the_tools(string, k):
    import textwrap
    text = textwrap.wrap(string, k)
    for i in text:
        temp = []
        for j in range(len(i)):
            if i[j] not in temp:
                temp.append(i[j])
        print("".join(temp))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
