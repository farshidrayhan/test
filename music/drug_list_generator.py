def list_filler(list):
    return_this_list = [0] * 882

    for i in list:
        # print(i)
        return_this_list[int(i)] = 1

    return return_this_list