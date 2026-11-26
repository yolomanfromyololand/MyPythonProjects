# Author: Yaroslav
# Date: 2026-11-16
# Purpose: Practice drawing lines on a chart, changing their colour, style and markers, and adding axis labels, a legend and grid lines.

import matplotlib.pyplot as plt


def plot_two_lines(x, y1, y2, filename):
    plt.figure()
    plt.plot(x, y1, color="blue", linestyle="-", marker="o", label="y = 2x")   # done for you
    plt.title("Linear vs Quadratic Growth")                                     # done for you
    # 1. Plot y2 against x: red, dashed line ("--"), square markers ("s"), label "y = x^2"
    plt.plot(x, y2, color="red", linestyle="--", marker="s", label="y = x^2")
    # 2. Set the x-axis label to "x" and the y-axis label to "y"
    plt.xlabel("x")
    plt.ylabel("y")
    # 3. Add a legend and grid lines
    plt.legend()
    plt.grid(True)
    plt.savefig(filename)
    plt.close()
    print("Saved", filename)


def main():
    x = [1, 2, 3, 4, 5]
    y1 = [2, 4, 6, 8, 10]
    y2 = [1, 4, 9, 16, 25]
    plot_two_lines(x, y1, y2, "two_lines.png")


main()
