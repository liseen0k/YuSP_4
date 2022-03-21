with open("input.txt") as textFile:
    lines = [line.split() for line in textFile]
    textFile.close()
print("Input text: " + lines.__str__())


def check(t_list, i):
    if t_list[i] == '=' and t_list[i-1] == t_list[i+1] and t_list[i+2] == '+' and t_list[i+3] == '1':
        return True
    else:
        return False


def search(text_list):
    index_list = []
    for i in range(len(text_list)):
        for j in range(len(text_list[i])):
            if check(text_list[i], j):
                index_list.append(i)
    return index_list


def copy_suitable_str(text_list, index_list):
    copied_str = []
    for i in range(len(index_list)):
        s = text_list[index_list[i]][:]
        copied_str.append(s)
    return copied_str


def change(text_list, index_list, changed_str):
    for i in range(len(index_list)):
        text_list[index_list[i]] = changed_str[i]


def change_str(copied_str):
    changed_str = []
    for i in range(len(copied_str)):
        for j in range(len(copied_str[i])):
            if (copied_str[i][j] == '=' and copied_str[i][j-1] == copied_str[i][j+1] and copied_str[i][j+2] == '+'
                    and copied_str[i][j+3] == '1'):
                c_list_b = copied_str[i][:j-1]
                c_list_c = c_list_b + [copied_str[i][j-1]+'++']
                changed_str.append(c_list_c)
    return changed_str


i_list = search(lines)
print("Index of suitable str: " + i_list.__str__())
s = copy_suitable_str(lines, i_list)
print("Copy of suitable str: " + s.__str__())
c = change_str(s)
print("Changed str: " + c.__str__())
change(lines, i_list, c)
print("Changed text: " + lines.__str__())

with open('output.txt', 'w') as testfile:
    for row in lines:
        testfile.write(' '.join([str(a) for a in row]) + '\n')
testfile.close()





