import copy
from ext import get_ext_list


def pol_mul(c_list, init_ext_list, str_res, curr_a):
    ext_list = get_ext_list(init_ext_list)
    str_add_v = " + (" + str(c_list[curr_a - 1]) + " * "
    for n_curr in range(len(ext_list)):
        str_add_v += "x" + str(n_curr) + "^" + str(ext_list[n_curr])
        if n_curr != len(ext_list) - 1:
            str_add_v += " * "
    str_res += str_add_v + ")"
    return str_res


def calc_pol(c_list, pol_ext, nv, n_call, ext_list, str_res, curr_a):
    n_call_new = n_call + 1
    new_ext_list = copy.deepcopy(ext_list)
    new_ext_list.append(0)
    for i in range(pol_ext + 1):
        new_ext_list[-1] = i
        if n_call_new == nv:
            curr_a += 1
            str_res = pol_mul(c_list, new_ext_list, str_res, curr_a)
        else:
            str_res, curr_a = calc_pol(c_list, i, nv, n_call_new, new_ext_list, str_res, curr_a)
    return str_res, curr_a


def print_polynomial(c, pol_ext, nv):
    print("coefficients list - ", c)
    str_res, curr_a = calc_pol(c, pol_ext, nv, 0, [], "", 0)
    print("polynomial = " + str_res[3:])
