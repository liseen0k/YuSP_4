with open("input.txt") as textFile:
    lines = [line.split() for line in textFile]
    textFile.close()
print(lines.__str__())


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
        s = text_list[index_list[i]].copy
        copied_str.append(s)
    return copied_str


# t_list = ['a', 'a', '=', 'a', '+', '1']
# for i in range(1, len(t_list)-3):
#     print(check(t_list, i))

i_list = search(lines)
print(i_list.__str__())
s = copy_suitable_str(lines, i_list)
print(s.__str__())


# def change(text_list, index_list):


