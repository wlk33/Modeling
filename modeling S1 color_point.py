
from point import Point # point is the file, Point is the class
import random

class ColorPoint(Point):
    def __init__(self, x, y, color):
        """
        Initialize a ColorPoint with x, y, and color.
        """
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        """
        Return a string representation of the ColorPoint.
        """
        return f"<{self.x}, {self.y}>({self.color})"


if __name__ == "__main__":
    color_points = []
    colors = ["red", "blue", "green", "yellow", "black", "white", "purple"]
    for _ in range(5):
        p = ColorPoint(
            random.randint(-100, 100),
            random.randint(-100, 100),
            random.choice(colors))
        color_points.append(p)

    print("Random Color Points")
    print(color_points)
    color_points.sort()
    print("Sorted Color Points")
    print(color_points)
