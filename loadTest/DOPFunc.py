def get_name_list():
    list_of_name = []
    with open('../server/NameList.txt', 'r') as NameList:
        for line in NameList:
            list_of_name.append(line[:-1])
    return list_of_name


