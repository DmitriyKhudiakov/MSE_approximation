import copy
from ext import get_ext_list


def pol_mul(x_list, c_list, init_ext_list, sum_v, curr_a):
    ext_list = get_ext_list(init_ext_list)
    sum_add_v = c_list[curr_a - 1]
    for n_curr in range(len(ext_list)):
        sum_add_v *= x_list[n_curr] ** ext_list[n_curr]
    sum_v += sum_add_v
    return sum_v


def calc_pol(x_list, c_list, pol_ext, nv, n_call, ext_list, sum_v, curr_a):
    n_call_new = n_call + 1
    new_ext_list = copy.deepcopy(ext_list)
    new_ext_list.append(0)
    for i in range(pol_ext + 1):
        new_ext_list[-1] = i
        if n_call_new == nv:
            curr_a += 1
            sum_v = pol_mul(x_list, c_list, new_ext_list, sum_v, curr_a)
        else:
            sum_v, curr_a = calc_pol(x_list, c_list, i, nv, n_call_new, new_ext_list, sum_v, curr_a)
    return sum_v, curr_a


def polynomial(ext, x_list, c_list):
    num_var = len(x_list)
    if num_var == 0:
        print("Number of variables is 0")
        return None
    else:
        res, a_n_last = calc_pol(x_list, c_list, ext, num_var, 0, [], 0.0, 0)
        return res
