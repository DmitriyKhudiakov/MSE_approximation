import copy
import numpy as np
from ext import get_ext_list


def b_mul(b, exp_list, init_ext_list):
    sum_add_v_all = 0.0
    ext_list = get_ext_list(init_ext_list)
    for curr_exp in exp_list:
        sum_add_v = curr_exp[-1]
        for n_curr in range(len(ext_list)):
            sum_add_v *= curr_exp[n_curr] ** ext_list[n_curr]
        sum_add_v_all += sum_add_v
    b.append(sum_add_v_all)
    return b


def calc_b(exp_list, b, pol_ext, nv, n_call, ext_list):
    n_call_new = n_call + 1
    new_ext_list = copy.deepcopy(ext_list)
    new_ext_list.append(0)
    for i in range(pol_ext + 1):
        new_ext_list[-1] = i
        if n_call_new == nv:
            b = b_mul(b, exp_list, new_ext_list)
        else:
            b = calc_b(exp_list, b, i, nv, n_call_new, new_ext_list)
    return b


def a_mul(a, exp_list, init_ext_list):
    sum_add_v_all1 = 0.0
    ext_list = []
    for curr_init_list in init_ext_list:
        ext_list.append(get_ext_list(curr_init_list))
    for curr_exp in exp_list:
        sum_add_v = 1.0
        for curr_ext_list in ext_list:
            for n_curr in range(len(ext_list[0])):
                sum_add_v *= curr_exp[n_curr] ** curr_ext_list[n_curr]
        sum_add_v_all1 += sum_add_v
    a.append(sum_add_v_all1)
    return a


def calc_a(exp_list, a, pol_ext, nv, n_call, ext_list, dim, real_pol_ext):
    n_call_new = n_call + 1
    new_ext_list = copy.deepcopy(ext_list)
    new_ext_list[dim].append(0)
    for i in range(pol_ext + 1):
        new_ext_list[dim][-1] = i
        if (n_call_new == nv) and (dim != 0):
            a = calc_a(exp_list, a, real_pol_ext, nv, 0, new_ext_list, dim - 1, real_pol_ext)
        elif (n_call_new == nv) and (dim == 0):
            a = a_mul(a, exp_list, new_ext_list)
        else:
            a = calc_a(exp_list, a, i, nv, n_call_new, new_ext_list, dim, real_pol_ext)
    return a


def calc_approx(exp_data, pol_ext, nv):
    b = calc_b(exp_data, [], pol_ext, nv, 0, [])
    a = calc_a(exp_data, [], pol_ext, nv, 0, [[], []], 1, pol_ext)
    n_size = int(np.sqrt(len(a)))
    a = np.reshape(a, (n_size, n_size))
    try:
        c = np.linalg.solve(np.array(a), np.array(b))
        return c
    except np.linalg.LinAlgError:
        print("Singular matrix. Try to enter more experimental points.")
        return None
