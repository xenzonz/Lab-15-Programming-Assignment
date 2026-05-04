print("hello world")

"""
Docstring for Lab15_xenzonz-1.py
i. Lab 15: Plot a Math Formula
ii. Sam Cocquyt
iii. A program that uses matplotlib to plot a spiral
iv. No starter code
v. 5/3/2026
"""

import math
import matplotlib.pyplot as plt


def spiral_data():
    x_values = []
    y_values = []

    for degrees in range(0, 360):
        radians = math.radians(degrees)
        radius = degrees / 360

        x = radius * math.cos(radians)
        y = radius * math.sin(radians)

        x_values.append(x)
        y_values.append(y)
    
    return x_values, y_values

        

def create_spiral(x_values, y_values):
    plt.plot(x_values, y_values)
    plt.savefig("spiralplot.png")
    plt.show

def main():
    x_values, y_values = spiral_data()
    create_spiral(x_values, y_values)

if __name__ == "__main__":
    main()