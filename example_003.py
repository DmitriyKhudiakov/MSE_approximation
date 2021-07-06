import re
import numpy as np
import matplotlib.pyplot as plt
from polynomial import polynomial
from approximation import calc_approx
from print_polynomial import print_polynomial


def get_exp_data():
    with open("example_data_files\\housing.data", "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        if lines[i][0] == " ":
            lines[i] = lines[i][1:]
        lines[i] = re.sub("\n", "", lines[i])
        lines[i] = re.sub(" +", " ", lines[i])
        lines[i] = re.split(" ", lines[i])
    exp_data = []
    for line in lines:
        curr_set = []
        for curr_var in line:
            curr_set.append(float(curr_var))
        exp_data.append(curr_set)
    return exp_data


def root_mean_square_error_calc(exp_data, polynomial_extent, c):
    error = 0.0
    for curr_data in exp_data:
        error += (polynomial(polynomial_extent, curr_data[:-1], c) - curr_data[-1]) ** 2
    error = np.sqrt(error / len(exp_data))
    return error


def is_float(str_read):
    try:
        float(str_read)
        return True
    except ValueError:
        return False


def set_vars(l_lim, h_lim, str_read):
    is_ok = True
    value = None
    is_right = is_float(str_read)
    if is_right is True:
        val = float(str_read)
        if (val >= l_lim) and (val <= h_lim):
            value = val
            ret_str = "ok"
        else:
            is_ok = False
            ret_str = "Error: value is not in valid range"
    else:
        is_ok = False
        ret_str = "Error: Invalid input format "
    return ret_str, is_ok, value


def calc_mode(exp_data, polynomial_extent, c):
    print("Test mode. To exit enter - stop.")
    print("The input format is dotted. Example: 0.456")
    print("Enter characteristics:")
    characteristic_list = ["crime: crime rate per person by city. ",
                           "zn: proportion of residential land zoned for lots over 25,000 sq.ft.. ",
                           "indus: proportion of non-retail business acres per town. ",
                           "chas: Charles River dummy variable (= 1 if tract bounds river; 0 otherwise). ",
                           "nox: nitrogen oxides concentration (parts per 10 million). ",
                           "rm: average number of rooms per dwelling. ",
                           "age: proportion of owner-occupied units built prior to 1940. ",
                           "dis: weighted mean of distances to five Boston employment centres. ",
                           "rad: index of accessibility to radial highways. ",
                           "tax: full-value property-tax rate per $10,000. ",
                           "pt_ratio: pupil-teacher ratio by town. ",
                           "black: 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town. ",
                           "l_stat: lower status of the population (percent). "]
    lim_list = []
    for i in range(len(exp_data[0]) - 1):
        lim_list.append([min([curr_data[i] for curr_data in exp_data]), max([curr_data[i] for curr_data in exp_data])])
    while True:
        test_list = []
        for i in range(len(exp_data[0]) - 1):
            while True:
                enter_str = input(characteristic_list[i] + "limits(" + str(lim_list[i][0]) + "___"
                                  + str(lim_list[i][1]) + ") = ")
                if enter_str == "stop":
                    return None
                ret_str, is_ok, value = set_vars(lim_list[i][0], lim_list[i][1], enter_str)
                if is_ok:
                    test_list.append(value)
                    break
                else:
                    print(ret_str)
        print("RESULT:")
        print("med_v: median value of owner-occupied homes in $1000s. = " +
              str(polynomial(polynomial_extent, test_list, c)) + "\n")


def main():
    exp_data = get_exp_data()
    polynomial_extent = 1
    num_variables = 13
    use_test_percent = 90.0
    c = calc_approx(exp_data[:int(len(exp_data) * use_test_percent / 100.0)], polynomial_extent, num_variables)
    print_polynomial(c, polynomial_extent, num_variables)
    error = root_mean_square_error_calc(exp_data[int(len(exp_data) * use_test_percent / 100.0):], polynomial_extent, c)
    print("root_mean_square_error = ", error)
    calc_mode(exp_data[:int(len(exp_data) * use_test_percent / 100.0)], polynomial_extent, c)


if __name__ == "__main__":
    main()
