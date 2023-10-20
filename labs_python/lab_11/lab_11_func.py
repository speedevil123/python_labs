def read_file(path):
    f = open(path)
    contents = list(map(int, f.readlines()))
    f.close()
    return contents

def finding(list):
    # max_even = (list[0])
    # min = (list[0])

    # for elem in list:
    #     if((elem) > max_even and (elem) % 2 == 0):
    #         max_even = (elem)
    #     if((elem) < min):
    #         min = (elem)
    # max_min = [max_even, min]
    max_even_list = [x for x in list if x % 2 == 0]
    max_even = max(max_even_list)
    min_all = min(list)
    max_min = [max_even,min_all]
    return max_min

def result(list,path):
    f = open(path, 'w')

    #for elem in list:
    #    f.write(str(elem) + '\n')
    ls = map(str, list)
    ls = '\n'.join(ls)
    f.write(ls)
    f.close()
    return
