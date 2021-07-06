import numpy as np
import matplotlib.pyplot as plt
from polynomial import polynomial
from approximation import calc_approx
from print_polynomial import print_polynomial


def create_exp_data():
    x = np.linspace(0.0, 2.0 * np.pi, 15)
    y = np.cos(x) - x / 2.0
    return [[x_curr, y_curr] for x_curr, y_curr in zip(x, y)], x, y


def plot_graph(x_list, y_list, polynomial_extent, c):
    x = np.linspace(0.0, 2.0 * np.pi, 200)
    y = [polynomial(polynomial_extent, [x_curr], c) for x_curr in x]
    plt.grid()
    plt.plot(x, y, label="polynomial")
    plt.scatter(x_list, y_list, color="r", label="experimental points")
    plt.legend()
    plt.show()


def main():
    exp_data, x_list, y_list = create_exp_data()
    polynomial_extent = 5
    num_variables = 1
    c = calc_approx(exp_data, polynomial_extent, num_variables)
    print_polynomial(c, polynomial_extent, num_variables)
    plot_graph(x_list, y_list, polynomial_extent, c)


if __name__ == "__main__":
    main()
