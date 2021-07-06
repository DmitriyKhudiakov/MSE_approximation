

def get_ext_list(init_ext_list):
    ext_list = []
    for n in range(len(init_ext_list)):
        if n == len(init_ext_list) - 1:
            ext_list.append(init_ext_list[n])
        else:
            ext_list.append(init_ext_list[n] - init_ext_list[n + 1])
    return ext_list
