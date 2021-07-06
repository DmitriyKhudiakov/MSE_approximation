import numpy as np
import matplotlib.pyplot as plt
from polynomial import polynomial
from approximation import calc_approx
from print_polynomial import print_polynomial


def get_exp_data():
    points = []
    with open("example_data_files\\graph_test.txt") as file:
        for line in file.readlines():
            points.append(list(map(float, line.split(" "))))
    return [[point[1], point[2], point[0]] for point in points]


def plot_graph(exp_data, polynomial_extent, c):
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    step = 0.01
    x_list = [point[0] for point in exp_data]
    y_list = [point[1] for point in exp_data]
    z_list = [point[2] for point in exp_data]
    x_pol = np.arange(min(x_list), max(x_list), step)
    y_pol = np.arange(min(y_list), max(y_list), step)
    x_pol, y_pol = np.meshgrid(x_pol, y_pol)
    z_pol = np.array(polynomial(polynomial_extent, [x_pol, y_pol], c))
    ax.plot_wireframe(x_pol, y_pol, z_pol, linewidth=0.2, antialiased=False, label="polynomial")
    ax.scatter(x_list, y_list, z_list, color="r", label="experimental points")
    plt.legend()
    plt.show()


def main():
    exp_data = get_exp_data()
    polynomial_extent = 3
    num_variables = 2
    c = calc_approx(exp_data, polynomial_extent, num_variables)
    print_polynomial(c, polynomial_extent, num_variables)
    plot_graph(exp_data, polynomial_extent, c)


if __name__ == "__main__":
    main()
