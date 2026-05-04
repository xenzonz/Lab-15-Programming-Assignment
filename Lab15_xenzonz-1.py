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

def spiral_data() -> tuple[list[float], list[float]]:
    """
    Generate x and y coordinate lists for a spiral.

    Returns:
        A tuple containing the x-values list and y-values list.
    """
    x_values: list[float] = []
    y_values: list[float] = []

    for degrees in range(0, 1440):
        radians: float = math.radians(degrees)
        radius: float = degrees / 360

        x: float = radius * math.cos(radians)
        y: float = radius * math.sin(radians)

        x_values.append(x)
        y_values.append(y)
    
    return x_values, y_values

def create_spiral(x_values: list[float], y_values: list[float]) -> None:
    """
    Create and save a spiral plot.

    Args:
        x_values: The list of x-coordinates.
        y_values: The list of y-coordinates.
    """
    plt.style.use("bmh")

    plt.plot(x_values, y_values, color="red", linestyle="dashdot", linewidth=3)
    
    plt.title("Spiral Graph")
    plt.xlabel("X Values")
    plt.ylabel("Y Values")
    plt.grid(True)

    plt.savefig("spiral_plot.png")
    plt.show

def main() -> None:
    """
    Run the spiral graph program.
    """
    x_values, y_values = spiral_data()
    create_spiral(x_values, y_values)

if __name__ == "__main__":
    main()