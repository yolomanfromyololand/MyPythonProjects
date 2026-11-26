# Author: Yaroslav
# Date: 2026-11-16
# Purpose: Practice creating a bar chart, a scatter plot and a histogram, and understanding when to use each one.

import matplotlib.pyplot as plt


def plot_bar(products, sales, filename):        # done for you
    plt.figure()
    plt.bar(products, sales, color="orange")
    plt.title("Product Sales Comparison")
    plt.xlabel("Product")
    plt.ylabel("Sales (units)")
    plt.savefig(filename)
    plt.close()
    print("Saved", filename)


def plot_scatter(x, y, filename):
    # Follow the same steps as plot_bar(), but:
    # - draw a scatter plot with green dots (c="green"), size 100 (s=100) and alpha=0.6
    # - title "Car Age vs Speed", x-axis label "Car age (years)", y-axis label "Speed (km/h)"
    plt.figure()
    plt.scatter(x, y, c="green", s=100, alpha=0.6)
    plt.title("Car Age vs Speed")
    plt.xlabel("Car age (years)")
    plt.ylabel("Speed (km/h)")
    plt.savefig(filename)
    plt.close()
    print("Saved", filename)


def plot_histogram(daily_sales, filename):
    # Follow the same steps as plot_bar(), but:
    # - draw a histogram with 5 bins and black edges (edgecolor="black")
    # - title "Distribution of Daily Sales", x-axis label "Daily sales (units)",
    #   y-axis label "Number of days"
    plt.figure()
    plt.hist(daily_sales, bins=5, edgecolor="black")
    plt.title("Distribution of Daily Sales")
    plt.xlabel("Daily sales (units)")
    plt.ylabel("Number of days")
    plt.savefig(filename)
    plt.close()
    print("Saved", filename)


def main():
    products = ["Coffee", "Tea", "Juice", "Soda"]
    sales = [150, 120, 90, 60]
    plot_bar(products, sales, "bar_chart.png")

    ages = [5, 7, 8, 7, 6, 9, 5, 6]
    speeds = [99, 86, 87, 88, 100, 86, 103, 87]
    plot_scatter(ages, speeds, "scatter_plot.png")

    daily_sales = [20, 15, 25, 18, 30, 12, 22, 28, 16, 14, 19, 21]
    plot_histogram(daily_sales, "histogram.png")


main()

# A bar chart compares sales for separate product categories.
# A histogram groups the numeric daily sales into ranges and shows how many days
# fall in each range, making the distribution of daily sales easier to see.
